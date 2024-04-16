from telebot import types


def exit_to_nutrient_markup():
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('exit'))
    return markup
