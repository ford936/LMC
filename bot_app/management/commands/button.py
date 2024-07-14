from telebot import types


async def main_markup() -> types.ReplyKeyboardMarkup:
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Заполнить заявку')
    markup.add(btn1)
    return markup


async def auth_markup() -> types.ReplyKeyboardMarkup:
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Продолжить', request_contact=True)
    markup.add(btn1)
    return markup


async def choice_service() -> types.ReplyKeyboardMarkup:
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('РВП')
    btn2 = types.KeyboardButton('ВНЖ')
    btn3 = types.KeyboardButton('Гражданство')
    btn4 = types.KeyboardButton('Запрет')
    btn5 = types.KeyboardButton('Исковое заявление')
    btn6 = types.KeyboardButton('Жалоба')
    btn7 = types.KeyboardButton('Алименты')
    btn8 = types.KeyboardButton('Другое')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
    return markup


async def yes_or_no() -> types.ReplyKeyboardMarkup:
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Да')
    btn2 = types.KeyboardButton('Нет')
    markup.add(btn1, btn2)
    return markup