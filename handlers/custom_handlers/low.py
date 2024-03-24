from telebot.types import Message

from api.core import url, headers, params
from keyboards.reply.low_nutrient_markup import low_reply_nutrient, nutrient_mapping
from loader import bot
from states.low_state import LowState
from api import main_api


@bot.message_handler(commands=['low'])
def low_func(message: Message) -> None:
    user_id = message.from_user.id
    chat_id = message.chat.id
    bot.set_state(user_id, LowState.nutrient, chat_id)
    bot.send_message(message.from_user.id, f'Выбери питательное вещество, минимальное количество которого должно содержать блюдо в граммах\n- '
                                           f'белок\n- '
                                           f'углеводы\n- кальций\n- фосфор', reply_markup=low_reply_nutrient())


@bot.message_handler(state=LowState.nutrient)
def get_nutrient(message: Message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    if message.text.strip().lower() in nutrient_mapping:
        nutrient = nutrient_mapping[message.text.strip().lower()]
        bot.send_message(user_id, 'Спасибо, записал.\nТеперь введи его количество в блюде')
        bot.set_state(user_id, LowState.value, chat_id)
        with bot.retrieve_data(user_id, chat_id) as data:
            data['nutrient'] = nutrient
    else:
        bot.send_message(message.from_user.id, 'пожалуйста, нажми на одну из кнопок')


@bot.message_handler(state=LowState.value)
def get_value(message: Message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    if message.text.isdigit():
        bot.set_state(user_id, LowState.dish, chat_id)
        with bot.retrieve_data(user_id, chat_id) as data:
            data['value'] = message.text
    else:
        bot.send_message(message.from_user.id, 'Количество может быть положительным числом')

    response = (main_api.dish_low_protein("GET", url, headers, params, data['value'], data['nutrient'])).json()
    if response:
        max_dishes = min(10, len(response))
        titles = [f"{i + 1}. {dish['title']}" for i, dish in enumerate(response[:max_dishes])]

        bot.send_message(user_id, 'Спасибо, держи список блюд:\n')
        bot.send_message(user_id, '\n'.join(titles))
        bot.send_message(user_id, 'Введи номер блюда, чтобы получить рецепт')
    else:
        bot.send_message(user_id, 'Извините, не удалось найти блюда по вашему запросу. Введи другое количество:')
        bot.set_state(user_id, LowState.value, chat_id)


@bot.message_handler(state=LowState.dish)
def get_dish(message: Message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    if message.text.isalpha():
        bot.send_message(user_id, 'Спасибо, держи ссылку на рецепт блюда')
        bot.set_state(user_id, None, chat_id)
        with bot.retrieve_data(user_id, chat_id) as data:
            data['dish'] = message.text
    else:
        bot.send_message(message.from_user.id, 'Пожалуйста, введи название одного из предложенных блюд')
