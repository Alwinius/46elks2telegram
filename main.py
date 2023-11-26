from bottle import request, post, run, HTTPResponse
from telegram import Bot
import configparser

from telegram.parsemode import ParseMode


@post('/sms')
def sms():
    incoming_message = request.forms.get('message')
    sender = request.forms.get('from')
    message = "New SMS received from "+sender+":\n"+incoming_message
    bot.send_message(chat_id=config["chatId"], parse_mode=ParseMode.MARKDOWN_V2, text=message)
    print(message)
    return HTTPResponse(status=200)


if __name__ == '__main__':
    _parser = configparser.ConfigParser()
    _parser.read("config.ini")
    config = _parser['DEFAULT']
    bot = Bot(token=config["BotToken"])
    run(host='0.0.0.0', port=8080)
