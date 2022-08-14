import asyncio
from aiogram import Bot, Dispatcher, executor, types
import configparser
from course_stat import *

config = configparser.ConfigParser()
config.read("config.ini")
TOKEN = config['Telegram']['TOKEN']

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
counter_day_notif = 0
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    global user_id
    user_id = message.chat.id
    await message.answer("Привет!\n введите команду /help, что бы ознакомиться со список команд!")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    global user_id
    user_id = message.chat.id
    await message.answer(
        "Доступны следующие функции:\n - /courses - показать актуальные курсы валют \n - /notif_course - "
        "Присылать актуальный курс каждое утро и вечер (09:00 и 21:00) \n - /stop_notif - отключить рассылку "
        "\n - /notif_change_course - включить оповещение при смене курса \n"
        " - /stop_forward_course - отключить оповещение при смене курса \n - /send_course_sheet - отправка файла БД")


@dp.message_handler(commands=['courses'])
async def process_courses_command(message: types.Message):
    global usd_pars_list, eur_pars_list
    usd_pars_list = usd_pars()
    eur_pars_list =eur_pars()
    await message.answer(f"🇺🇸 Доллар:\nпокупка: {usd_pars_list[0]}, продажа: {usd_pars_list[1]}, чёрный: {usd_pars_list[2]}"
                         f" \n🇪🇺 Евро:\nпокупка: {eur_pars_list[0]}, продажа: {eur_pars_list[1]}, чёрный: {eur_pars_list[2]}")


@dp.message_handler(commands=['notif_course'])
async def process_notif_course(message: types.Message):
    global counter_day_notif, usd_pars_list, eur_pars_list, timenow
    usd_pars_list = usd_pars()
    eur_pars_list = eur_pars()
    counter_day_notif = 0
    await message.answer(f"Ежедневное оповещение курса (в 09:00 и в 21:00) включено!")
    while counter_day_notif == 0:
        timenow = datetime.datetime.today().strftime("%H:%M")
        if timenow == '21:00' or timenow == '09:00':
            save_course(usd_pars, eur_pars)
            await message.answer(
                f"🇺🇸 Доллар:\nпокупка: {usd_pars_list[0]}, продажа: {usd_pars_list[1]}, чёрный: {usd_pars_list[2]}"
                f" \n🇪🇺 Евро:\nпокупка: {eur_pars_list[0]}, продажа: {eur_pars_list[1]}, чёрный: {eur_pars_list[2]}")
            await asyncio.sleep(45)
        else:
            await asyncio.sleep(45)


@dp.message_handler(commands=['stop_notif'])
async def process_notif_course(message: types.Message):
    await message.answer(f"Остановлена!")
    global counter_day_notif
    counter_day_notif = 1


@dp.message_handler(commands=['notif_change_course'])
async def notif_change_course(message: types.Message):
    await message.answer(f"Оповещение о смене курса в пределах 10 копеек включено!")
    global counter_change_course
    counter_change_course = 0
    while counter_change_course == 0:
        if forward_stats(usd_pars, eur_pars):
            #pass
            await asyncio.sleep(60)
        else:
            await message.answer(f"курс изменился, данные занесены в таблицу. Для просмотре актуального курса /courses")


@dp.message_handler(commands=['stop_forward_course'])
async def stop_forward_course(message: types.Message):
    await message.answer(f"Остановлена!")
    global counter_change_course
    counter_change_course = 1


@dp.message_handler(commands=['send_course_sheet'])
async def send_course_sheet(message: types.Message):
    await message.answer(f"Отправляем файл")
    await message.answer_document(open('sheet_course.csv', 'rb'))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)