from telebot import types


def create_default_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(types.KeyboardButton('Hello \U0001F44B'))
    return keyboard
