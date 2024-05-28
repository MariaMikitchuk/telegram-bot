from telebot.types import Message

from database.core import crud
from database.models import History
from loader import bot


@bot.message_handler(commands=['history'])
def history_func(message: Message) -> None:
    user_id = message.from_user.id
    queries = (History.select().where(History.user_id == user_id).order_by(
        History.created_at.desc()).limit(10))
    history = "\n".join(
        [f"{query.created_at.strftime('%d-%m-%Y %H:%M:%S')} - {query.message}" for
         query
         in queries])
    bot.send_message(user_id, f"History of your last 10 queries:\n{history}")
    crud.create({"user_id": user_id, "message": "/history"})
