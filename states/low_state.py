from telebot.handler_backends import State, StatesGroup


class LowState(StatesGroup):
    nutrient = State()
    value = State()
    dish = State()
