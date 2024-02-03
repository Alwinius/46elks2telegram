# 46elks to telegram

This python script/telegram bot forwards SMS received from 46elks to a
specified Telegram account.

## Functionality

Currently, SMS will be forwarded to a telegram account. The other direction
might be implemented later. Doing calls via Telegram might also be cool but sounds 
hard to implement.

## Prerequisites

You need to have a server on the internet (or a port forward to your local network) 
and that server needs to be able to run docker containers.

## Setup

1. Create a Telegram bot by messaging BotFather
1. Obtain your chat_id by messaging your bot and querying 
the Telegram API manually (e.g. open `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates`)
1. Clone this repository and copy `config.ini.example` to `config.ini`
1. Fill in your chat_id and bot token in `config.ini`
1. Run the bot with `docker compose up -d`
1. Configure your server's IP and port 8080 (by default) in 46elks as the webhook
endpoint like so: `http://your_server_host:8080/sms`

## Security

The default configuration is not very secure. The connection between 46elks
and your server will not be encrypted and our webhook API is easily accessible 
on a common port.

You can alternatively use a different port (easy but not much more secure), or put a reverse
proxy in front. This takes care of TLS encryption and can hide your
API behind a random URL.

### Reverse Proxy

1. Install nginx and certbot
2. Setup DNS entry for your domain example.com to point to your server's IP
3. Run ``certbot certonly --nginx -d example.com`` to get a TLS certificate for your domain
4. Modify the docker-compose.yaml port declaration to open the port only on localhost:
```
    ports:
        - "127.0.0.1:8080:8080"
```
5. Use the following nginx configuration snippet to expose the bot's endpoint at https://example.com/completely-secure-hidden-string/:
```
server {
    server_name example.com;
    # other configuration about ports and certificates, check the default
    location /completely-secure-hidden-string/ {
        proxy_pass http://127.0.0.1:8080/;
        proxy_set_header       Host $host;
        proxy_pass_header Server;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_buffering off;
    }
}
```
6. Configure https://example.com/completely-secure-hidden-string/sms as webhook URL in 46elks
7. Replace `completely-secure-hidden-string` with something actually random to prevent strangers from finding your API
