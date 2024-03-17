from telebot.types import Message

from keyboards.reply.commands import command_markup
from keyboards.reply.hello import create_default_keyboard
from loader import bot


@bot.message_handler(commands=["start", "hello-world"])
def bot_start(message: Message):
    keyboard = create_default_keyboard()
    bot.reply_to(message, f"Привет, {message.from_user.full_name}!\n Отправь мне 'привет', чтобы продолжить работу", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text.lower().startswith('привет'))
def hello_handler(message):
    keyboard = command_markup()
    bot.send_message(message.from_user.id, 'Я бот, который поможет найти тебе рецепты по заданному содержанию питательных веществ.\nВыбери '
                                           'параметры поиска:\n- с минимальным количеством(low)\n- с максимальным количеством(high)...',
                     reply_markup=keyboard)
