from telebot import types


def command_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    low_button = types.KeyboardButton('/low')
    high_button = types.KeyboardButton('/high')
    history_button = types.KeyboardButton('/history')
    markup.row(low_button, high_button)
    markup.row(history_button)
    return markup
