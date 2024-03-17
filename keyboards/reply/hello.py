from telebot import types


def create_default_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton('Привет \U0001F44B'))
    return keyboard
