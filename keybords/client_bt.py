from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton("/Информация_про_бота")
b2 = KeyboardButton("/Список_участников")
b3 = KeyboardButton("/Краткое_описание_участников")
b4 = KeyboardButton("/Выбор")
b5 = KeyboardButton("Поделиться номером", request_contact=True)
b6 = KeyboardButton("Отправить где я", request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).add(b2).insert(b3).add(b4).row(b5,b6)