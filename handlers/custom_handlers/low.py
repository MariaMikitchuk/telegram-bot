from loader import bot
from states.low_state import LowState
from telebot.types import Message
from keyboards.reply.low_nutrient import low_reply_nutrient


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


@bot.message_handler(state=LowState.dish)
def get_dish(message: Message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    if message.text.isalpha():
        bot.send_message(message.from_user.id, 'Спасибо, держи ссылку на рецепт блюда')
        with bot.retrieve_data(user_id, chat_id) as data:
            data['dish'] = message.text
    else:
        bot.send_message(message.from_user.id, 'Пожалуйста, введи название одного из предложенных блюд')
