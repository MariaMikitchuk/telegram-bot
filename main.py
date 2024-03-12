import telebot

from handlers.default_handlers.start import bot_start
from handlers.default_handlers.help import bot_help
from handlers.default_handlers.echo import bot_echo
from config_data.config import BOT_TOKEN


bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start', 'hello-world'])
def start_handler(message):
    bot_start(message)


@bot.message_handler(func=lambda message: message.text.lower() == 'привет')
def hello_handler(message):
    bot_start(message)


@bot.message_handler(commands=['help'])
def help_handler(message):
    bot_help(message)


@bot.message_handler()
def help_handler(message):
    bot_echo(message)


if __name__ == '__main__':
    bot.polling(none_stop=True)
