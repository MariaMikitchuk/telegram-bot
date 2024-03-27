from telebot import types

nutrient_mapping = {
    'белок': 'protein',
    'углеводы': 'carbs',
    'кальций': 'calcium',
    'фосфор': 'phosphorus'
}


def low_reply_nutrient():
    markup = types.ReplyKeyboardMarkup()
    row_1 = []
    row_2 = []
    for russian_name, english_name in nutrient_mapping.items():
        button = types.KeyboardButton(russian_name)
        if len(row_1) < 2:
            row_1.append(button)
        else:
            row_2.append(button)
    markup.row(*row_1)
    markup.row(*row_2)
    return markup


def exit_to_nutrient_markup():
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('exit'))
    return markup
