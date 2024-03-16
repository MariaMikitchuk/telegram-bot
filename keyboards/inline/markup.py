from telebot import types


def create_default_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.InlineKeyboardButton('/help'))
    return keyboard
