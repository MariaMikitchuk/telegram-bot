from telebot import types


def exit_to_nutrient_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(types.KeyboardButton('exit'))
    return markup
