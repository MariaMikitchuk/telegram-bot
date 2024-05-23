from telebot import types

nutrient_mapping = ['sugar', 'fat', 'cholesterol', 'carbs']


def high_reply_nutrient():
    markup = types.ReplyKeyboardMarkup()
    row_1 = []
    row_2 = []
    for name in nutrient_mapping:
        button = types.KeyboardButton(name)
        if len(row_1) < 2:
            row_1.append(button)
        else:
            row_2.append(button)
    markup.row(*row_1)
    markup.row(*row_2)
    return markup

