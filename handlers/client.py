from aiogram import Dispatcher, types
from create_bot import dp, bot 
from keybords import kb_client
from data_base import sqlite_db





# @dp.message_handler(commands=["start", "help"])
async def command_start(message:types.Message):
    try:
        await bot.send_message(message.from_user.id, "Приветствуем!", reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply("Общение с ботом в ЛС, напишите ему:\nhttp://t.me/BezBabPacany_bot")

# @dp.message_handler(commands="Информация_про_бота")
async def open_command(message:types.Message):
    await bot.send_message(message.from_user.id, "Этот бот поможет вам найти молодого успешного парня или вступить в ряды этих парней")

# @dp.message_handler(commands="Список_участников")
async def open2_command(message:types.Message):
    await bot.send_message(message.from_user.id, "Илья Рыбакб, Александр Час, Александр Сашко, Александр Луганский, Лексус, Паблитто, Гаран, Богдан")

# @dp.message_handler(commands="Краткое_описание_участников")
async def open3_command(message:types.Message):
    await bot.send_message(message.from_user.id, "Илья рыбак: 19 лет, создатель бота\nАлександр Час: 20 лет, дизайнер\nАлександр Сашко: 20 лет, программист, семьянин, гнёт штанги пальцами\nАлександр Луганский: 20 лет, программист, футболист, душа компании, чувствует\nЛексус: 19 лет, программист, танцор, геймер\nПаблитто: 18 лет, спортсмен, бейсболист, в какой-то степени испанец\nГаран: 18 лет, спортсмен, бейсболист, много ест\nБогдан: 19 лет, математик ")

# @dp.message_handler(commands=["Выбор"])
async def open4_command(message:types.Message):
    await sqlite_db.sql_read(message)


def redister_handlers_client(dp:Dispatcher):
    dp.register_message_handler(command_start, commands=["start", "help"])
    dp.register_message_handler(open_command, commands=["Информация_про_бота"])
    dp.register_message_handler(open2_command, commands=["Список_участников"])
    dp.register_message_handler(open3_command, commands=["Краткое_описание_участников"])
    dp.register_message_handler(open4_command, commands=["Выбор"])
