from telebot.types import Message

from keyboards.reply.low_nutrient import low_reply_nutrient
from loader import bot
from states.low_state import LowState


@bot.message_handler(commands=['low'])
def low_func(message: Message) -> None:
    user_id = message.from_user.id
    chat_id = message.chat.id
    bot.set_state(user_id, LowState.nutrient, chat_id)
    bot.send_message(message.from_user.id, f'Выбери питательное вещество, минимальное количество которого должно содержать блюдо\n- белок\n- '
                                           f'углеводы\n- кальций\n- магний', reply_markup=low_reply_nutrient())


@bot.message_handler(state=LowState.nutrient)
def get_nutrient(message: Message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    if message.text.strip().lower() in ['белок', 'углеводы', 'кальций', 'магний']:
        bot.send_message(message.from_user.id, 'Спасибо, записал.\nТеперь введи его количество в блюде')
        bot.set_state(user_id, LowState.value, chat_id)
        with bot.retrieve_data(user_id, chat_id) as data:
            data['nutrient'] = message.text
    else:
        bot.send_message(message.from_user.id, 'пожалуйста, нажми на одну из кнопок')


@bot.message_handler(state=LowState.value)
def get_value(message: Message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    if message.text.isdigit():
        bot.send_message(message.from_user.id, 'Спасибо, держи список блюд []\nОтправь мне название блюда, если хочешь получить рецепт')
        bot.set_state(user_id, LowState.dish, chat_id)
        with bot.retrieve_data(user_id, chat_id) as data:
            data['value'] = message.text
    else:
        bot.send_message(message.from_user.id, 'Количество может быть положительным числом')


@bot.message_handler(state=LowState.dish)
def get_dish(message: Message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    if message.text.isalpha():
        bot.send_message(message.from_user.id, 'Спасибо, держи ссылку на рецепт блюда')
        bot.set_state(user_id, None, chat_id)
        with bot.retrieve_data(user_id, chat_id) as data:
            data['dish'] = message.text
    else:
        bot.send_message(message.from_user.id, 'Пожалуйста, введи название одного из предложенных блюд')
