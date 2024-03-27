from telebot.types import Message

from keyboards.reply.commands import command_markup
from keyboards.reply.hello import create_default_keyboard
from loader import bot


@bot.message_handler(commands=["start", "hello-world"])
def bot_start(message: Message):
    keyboard = create_default_keyboard()
    bot.reply_to(message, f"Hello, {message.from_user.full_name}!\n Send me 'hello', to continue work", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text.lower().startswith('hello'))
def hello_handler(message):
    keyboard = command_markup()
    bot.send_message(message.from_user.id, 'I am a bot that will help you find recipes for a given nutrient content.\nchoose search parameters:\n- '
                                           'with the minimum amount(low)\n- with the maximum amount(high)...',
                     reply_markup=keyboard)
