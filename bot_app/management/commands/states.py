from telebot.asyncio_handler_backends import StatesGroup, State


class MyStates(StatesGroup):
    auth = State()
    auth_2 = State()
    name = State()
    surname = State()
    second_surname = State()
    country = State()
    phone = State()
    service = State()
    check = State()