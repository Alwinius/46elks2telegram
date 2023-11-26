from bottle import request, post, run, HTTPResponse
from telegram.constants import ParseMode
from telegram.ext import ApplicationBuilder
import configparser


@post('/sms')
def sms():
    incoming_message = request.forms.get('message')
    sender = request.forms.get('from')
    message = "New SMS received from "+sender+":\n"+incoming_message
    application.bot.send_message(chat_id=config["chatId"], parse_mode=ParseMode.MARKDOWN_V2, text=message)
    print("You have received an SMS")
    return HTTPResponse(status=200)


if __name__ == '__main__':
    _parser = configparser.ConfigParser()
    _parser.read("config.ini")
    config = _parser['DEFAULT']

    application = ApplicationBuilder().token(config["BotToken"]).build()
    run(host='0.0.0.0', port=8080)
