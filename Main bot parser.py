from datetime import datetime
import time
from threading import Thread
from course_pars_fun import *
from aiogram import Bot, Dispatcher, executor, types
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
TOKEN = config['Telegram']['TOKEN']

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
counter = 0
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    global user_id
    user_id = message.chat.id
    await message.answer("Привет!\n введите команду /help, что бы ознакомиться со список команд!")

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    global user_id
    user_id = message.chat.id
    await message.answer("Доступны следующие функции:\n - /courses - показать актуальные курсы валют \n - /notif_course - "
                         "Присылать актуальный курс раз в \n - /stop_notif - отключить рассылку")

@dp.message_handler(commands=['courses'])
async def process_courses_command(message: types.Message):
    await message.answer(f"🇺🇸 Доллар:\n{usd_pars()} \n🇪🇺 Евро:\n{eur_pars()}, \n🇬🇧󠁧󠁢󠁥󠁮󠁧󠁿 󠁧󠁢󠁥󠁮󠁧󠁿Фунты-стерлинги:\n{gbfunt_pars()}")

@dp.message_handler(commands=['notif_course'])
async def process_notif_course(message: types.Message):
    global counter
    counter = 0
    while counter == 0:
        await message.answer(f"🇺🇸 Доллар:\n{usd_pars()} \n🇪🇺 Евро:\n{eur_pars()}, \n🇬🇧󠁧󠁢󠁥󠁮󠁧󠁿 󠁧󠁢󠁥󠁮󠁧󠁿Фунты-стерлинги:\n{gbfunt_pars()}")
        time.sleep(3)

@dp.message_handler(commands=['stop_notif'])
async def process_notif_course(message: types.Message):
    await message.answer(f"Остановлена!")
    global counter
    counter = 1


if __name__ == '__main__':
    Thread(target=process_notif_course)
    executor.start_polling(dp, skip_updates=True)