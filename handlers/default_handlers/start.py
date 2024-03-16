from telebot.types import Message
from keyboards.inline.markup import create_default_keyboard
from loader import bot


@bot.message_handler(commands=["start", "hello-world"])
def bot_start(message: Message):
    keyboard = create_default_keyboard()
    bot.reply_to(message, f"Привет, {message.from_user.full_name}!", reply_markup=keyboard)

