from telebot import types
from telebot.types import Message

from api import main_api
from api.core import url, headers, params, url_dish, params_dish
from keyboards.reply.low_nutrient_markup import low_reply_nutrient, nutrient_mapping
from loader import bot
from states.low_state import LowState


@bot.message_handler(commands=['low'])
def low_func(message: Message) -> None:
    user_id = message.from_user.id
    chat_id = message.chat.id
    bot.set_state(user_id, LowState.nutrient, chat_id)
    bot.send_message(message.from_user.id, f'Choose a nutrient, the minimum amount of which should contain a dish in grams\n- '
                                           f'protein\n- '
                                           f'carbs\n- calcium\n- phosphorus', reply_markup=low_reply_nutrient())


@bot.message_handler(state=LowState.nutrient)
def get_nutrient(message: Message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    if message.text.strip().lower() in nutrient_mapping:
        nutrient = message.text.strip().lower()
        bot.send_message(user_id, 'Thanks, I wrote it down.\nNow enter the amount of it in the dish in grams',
                         reply_markup=types.ReplyKeyboardRemove())
        bot.set_state(user_id, LowState.value, chat_id)
        with bot.retrieve_data(user_id, chat_id) as data:
            data['nutrient'] = nutrient
    else:
        bot.send_message(message.from_user.id, 'Please press one of the buttons')


@bot.message_handler(state=LowState.value)
def get_value(message: Message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    if message.text.isdigit():
        bot.set_state(user_id, LowState.dish, chat_id)
        with bot.retrieve_data(user_id, chat_id) as data:
            data['value'] = message.text
    else:
        bot.send_message(message.from_user.id, 'The quantity can be a positive number')

    response, titles, id_dict, max_dishes = main_api.dish_low_nutrient("GET", url, headers, params, data['value'], data['nutrient'])
    if response:
        bot.id_dict = id_dict
        bot.max_dishes = max_dishes
        bot.send_message(user_id, 'Thanks, here is the list of dishes:\n')
        bot.send_message(user_id, '\n'.join(titles))
        bot.send_message(user_id, 'Enter the number of the dish to learn more about it')
    else:
        bot.send_message(user_id, "Sorry, I couldn't find the dishes according to your request. Enter another quantity:")
        bot.set_state(user_id, LowState.value, chat_id)


@bot.message_handler(state=LowState.dish)
def get_dish(message: Message):
    user_id = message.from_user.id
    chat_id = message.chat.id

    if message.text.isdigit() and 1 <= int(message.text) <= bot.max_dishes:
        bot.send_message(user_id, 'Thanks, get more information:')
        with bot.retrieve_data(user_id, chat_id) as data:
            data['dish'] = int(message.text)
    else:
        bot.send_message(user_id, 'Please enter the number of one of the suggested dishes')
    dish_id = bot.id_dict.get(data['dish'])
    url_id = url_dish.format(dish_id)
    summary, link = main_api.dish_low_summary("GET", url_id, headers, params_dish)
    bot.send_message(user_id, summary)
    bot.send_message(user_id, f'Search for the recipe by following the link {link}')
    bot.set_state(user_id, None, chat_id)

