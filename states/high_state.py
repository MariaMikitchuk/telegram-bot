from telebot.handler_backends import State, StatesGroup


class HighState(StatesGroup):
    nutrient = State()
    value = State()
    dish = State()
