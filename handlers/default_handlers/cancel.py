from telebot.types import Message

from keyboards.reply.commands import command_markup
from loader import bot


@bot.message_handler(state='*', commands=['cancel'])
def any_state(message: Message):
    """
    Cancel state
    """
    bot.send_message(message.chat.id, 'Your operation was cancelled',
                     reply_markup=command_markup())
    bot.delete_state(message.from_user.id, message.chat.id)
