from telebot import types


def command_markup():
    markup = types.ReplyKeyboardMarkup()
    low_button = types.KeyboardButton('/low')
    high_button = types.KeyboardButton('/high')
    markup.add(low_button, high_button)
    return markup
