from telebot import types


def low_reply_nutrient():
    markup = types.ReplyKeyboardMarkup()
    protein_button = types.KeyboardButton('белок')
    carbs_button = types.KeyboardButton('углеводы')
    calcium_button = types.KeyboardButton('кальций')
    magnesium_button = types.KeyboardButton('магний')
    markup.row(protein_button, carbs_button)
    markup.row(calcium_button, magnesium_button)
    return markup
