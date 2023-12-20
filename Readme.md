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
1. Obtain your chat_id by messaging your bot and and querying 
the Telegram API manually (e.g. open `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates`)
1. Clone this repository and copy `config.ini.example` to `config.ini`
1. Fill in your chat_id and bot token in `config.ini`
1. Run the bot with `docker compose up -d`
1. Configure your server's IP and port 8080 (by default) in 46elks as the webhook
endpoint like so: `http://your_server_host:8080/sms`

## Security

The default configuration is not very secure. The connection between 46elks
and your server will not be encrypted and the our webhook API is easily accessible 
on a common port.

You can alternatively use a different port (easy but much more secure), or put a reverse
proxy in front. This takes care of TLS encryption and can hide your
API behind a random URL. A sample configuration will be added here soon.