from telebot.handler_backends import State, StatesGroup


class LowState(StatesGroup):
    nutrition = State()
    value = State()
    dish = State()
