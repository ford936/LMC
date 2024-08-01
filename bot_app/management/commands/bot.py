import asyncio
from telebot.asyncio_storage import StateMemoryStorage
from telebot.async_telebot import AsyncTeleBot
from telebot.asyncio_filters import StateFilter, TextMatchFilter

from .states import MyStates
from .button import main_markup, choice_service, yes_or_no, auth_markup
from .mail import send_notification

import os
from dotenv import load_dotenv


load_dotenv()
tg_api_key = os.environ.get('TELEGRAM_TOKEN')

bot: AsyncTeleBot = AsyncTeleBot(tg_api_key, state_storage=StateMemoryStorage())


@bot.message_handler(commands=['start'])
async def get_contact(message):
    await bot.set_state(message.from_user.id, MyStates.auth, message.chat.id)
    await bot.send_message(message.chat.id, 'Вас приветствует LegalMigrationCentre. Для получения консультации '
                                            'заполните заявку. Нажимая "Продолжить" вы передадите первичные контактные данные, которые будут использованы для улучшения качества обратной связи.', reply_markup=await auth_markup())


@bot.message_handler(content_types=['contact'], state=MyStates.auth)
async def get_auth(message):
    async with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['tg_phone'] = '+' + message.contact.phone_number.replace("+", "")
    await bot.set_state(message.from_user.id, MyStates.auth_2, message.chat.id)
    await bot.send_message(message.chat.id, 'Вы успешно прошли авторизацию.', reply_markup=await main_markup())


@bot.message_handler(text=['Заполнить заявку'], state=MyStates.auth_2)
async def get_start(message):
    await bot.set_state(message.from_user.id, MyStates.name, message.chat.id)
    await bot.send_message(message.chat.id, 'Введите ваше имя')


@bot.message_handler(state=MyStates.name)
async def get_name(message):
    async with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['name'] = message.text
    await bot.set_state(message.from_user.id, MyStates.surname, message.chat.id)
    await bot.send_message(message.chat.id, 'Введите вашу фамилию')


@bot.message_handler(state=MyStates.surname)
async def get_second_surname(message):
    async with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['surname'] = message.text
    await bot.set_state(message.from_user.id, MyStates.second_surname, message.chat.id)
    await bot.send_message(message.chat.id, 'Введите ваше отчество (при наличии)')


@bot.message_handler(state=MyStates.second_surname)
async def get_country(message):
    async with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['second_surname'] = message.text
    await bot.set_state(message.from_user.id, MyStates.country, message.chat.id)
    await bot.send_message(message.chat.id, 'Гражданином какой страны вы являетесь?')


@bot.message_handler(state=MyStates.country)
async def get_service(message):
    async with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['country'] = message.text
    await bot.set_state(message.from_user.id, MyStates.service, message.chat.id)
    await bot.send_message(message.chat.id, 'Выберите категорию из предложенных.', reply_markup=await choice_service())


@bot.message_handler(text=['Другое'], state=MyStates.service)
async def get_service_another(message):
    await bot.set_state(message.from_user.id, MyStates.service, message.chat.id)
    await bot.send_message(message.chat.id, 'Напишите название необходимой услуги.', reply_markup=await choice_service())


@bot.message_handler(state=MyStates.service)
async def get_phone(message):
    async with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['service'] = message.text
    await bot.set_state(message.from_user.id, MyStates.phone, message.chat.id)
    await bot.send_message(message.chat.id, 'Введите контактный номер телефона.')


@bot.message_handler(state=MyStates.phone)
async def get_check(message):
    async with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['phone'] = message.text
    await bot.set_state(message.from_user.id, MyStates.check, message.chat.id)
    async with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['phone'] = message.text
        await bot.send_message(message.chat.id, f'Давайте сверим введенную информацию.\n Вас зовут {data["surname"]} '
                                                f'{data["name"]} {data["second_surname"]}.\n Гражданство {data["country"]}. \n '
                                                f'Контактный номер {data["phone"]}.\n Необходимая услуга: '
                                                f'{data["service"]}', reply_markup=await yes_or_no())


@bot.message_handler(state=MyStates.check)
async def get_final(message):
    if message.text == 'Да':
        async with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            try:
                send_mail = f'Новая заявка.\n{data["surname"]} {data["name"]} {data["second_surname"]}.\n' \
                            f'Гражданство {data["country"]}.\nКонтактный номер {data["phone"]}.\nНеобходимая услуга: {data["service"]}'\
                            f'\nTelegram: https://t.me/{data["tg_phone"]}'
            except:
                send_mail = f'Новая заявка.\n{data["surname"]} {data["name"]} {data["second_surname"]}.\n' \
                            f'Гражданство {data["country"]}.\nКонтактный номер {data["phone"]}.\nНеобходимая услуга: {data["service"]}'
            await send_notification(name=data["name"], surname=data["surname"], text=send_mail)
            await bot.set_state(message.from_user.id, MyStates.auth_2, message.chat.id)
            await bot.send_message(message.chat.id, 'Ваша заявка принята, ожидайте обратной связи', reply_markup=await main_markup())
            data.clear()
    else:
        await bot.set_state(message.from_user.id, MyStates.auth_2, message.chat.id)
        await bot.send_message(message.chat.id, 'Заполните заявку повторно', reply_markup=await main_markup())


bot.add_custom_filter(TextMatchFilter())
bot.add_custom_filter(StateFilter(bot))
asyncio.run(bot.infinity_polling(skip_pending=True, timeout=30))
