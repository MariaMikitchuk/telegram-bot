from telebot.types import Message

from api import main_api
from api.core import url, headers, params_dish, url_dish
from database.core import crud
from keyboards.reply.exit import exit_to_nutrient_markup
from keyboards.reply.high_nutrient_markup import high_reply_nutrient, nutrient_mapping
from loader import bot
from states.high_state import HighState


@bot.message_handler(commands=['high'])
def high_func(message: Message) -> None:
    user_id = message.from_user.id
    chat_id = message.chat.id
    bot.set_state(user_id, HighState.nutrient, chat_id)
    bot.send_message(user_id,
                     f'Choose a nutrient, the maximum amount of which should contain '
                     f'a dish in grams\n- '
                     f'sugar\n- '
                     f'fat\n- cholesterol\n- carbs',
                     reply_markup=high_reply_nutrient())
    crud.create({"user_id": user_id, "message": "/high"})


@bot.message_handler(state=HighState.nutrient)
def get_nutrient(message: Message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    if message.text.strip().lower() in nutrient_mapping:
        nutrient = message.text.strip().lower()
        bot.send_message(user_id,
                         'Thanks, I wrote it down.\nNow enter the amount of it in the '
                         'dish in grams or press "exit" to choose another '
                         'nutrient', reply_markup=exit_to_nutrient_markup())
        bot.set_state(user_id, HighState.value, chat_id)
        with bot.retrieve_data(user_id, chat_id) as data:
            data['nutrient'] = nutrient
            crud.create({"user_id": user_id, "message": message.text})
    else:
        bot.send_message(message.from_user.id, 'Please press one of the buttons')


@bot.message_handler(state=HighState.value)
def get_value(message: Message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    if message.text.strip().lower() == 'exit':
        crud.create({"user_id": user_id, "message": message.text})
        bot.set_state(user_id, HighState.nutrient, chat_id)
        bot.send_message(user_id, 'Choose nutrient:',
                         reply_markup=high_reply_nutrient())
    elif message.text.isdigit():
        bot.set_state(user_id, HighState.dish, chat_id)
        with bot.retrieve_data(user_id, chat_id) as data:
            data['value'] = message.text
            crud.create({"user_id": user_id, "message": message.text})
            response, titles, id_dict, max_dishes = main_api.dish_high_nutrient(
                "GET", url, headers, params_dish, data['value'], data['nutrient']
            )
            if response:
                bot.id_dict = id_dict
                bot.max_dishes = max_dishes
                bot.send_message(user_id, 'Thanks, here is the list of dishes:\n')
                bot.send_message(user_id, '\n'.join(titles))
                bot.send_message(user_id,
                                 'Enter the number of the dish to learn more about it')
            else:
                bot.send_message(user_id,
                                 "Sorry, I couldn't find the dishes according to your "
                                 "request. Enter another quantity:")
                bot.set_state(user_id, HighState.value, chat_id)
    else:
        bot.send_message(message.from_user.id, 'The quantity can be a positive number')


@bot.message_handler(state=HighState.dish)
def get_dish(message: Message):
    user_id = message.from_user.id
    chat_id = message.chat.id

    if message.text.isdigit() and 1 <= int(message.text) <= bot.max_dishes:
        bot.send_message(user_id, 'Thanks, get more information:')
        with bot.retrieve_data(user_id, chat_id) as data:
            data['dish'] = int(message.text)
            crud.create({"user_id": user_id, "message": message.text})
            dish_id = bot.id_dict.get(data['dish'])
            url_id = url_dish.format(dish_id)
            summary, link = main_api.dish_low_summary("GET", url_id, headers,
                                                      params_dish)
            bot.send_message(user_id, summary)
            bot.send_message(user_id,
                             f'Search for the recipe by following the link {link}')
            bot.set_state(user_id, None, chat_id)
    else:
        bot.send_message(user_id,
                         'Please enter the number of one of the suggested dishes')