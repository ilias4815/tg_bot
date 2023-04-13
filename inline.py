from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text

TOKEN = "5967754632:AAFZP5tiAjcHjbyHt-C484E1T-WvBC1xbLc"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

answ = dict()

urlkb = InlineKeyboardMarkup(row_width=1)
urlButton = InlineKeyboardButton(text="Ссылка", url="https://www.faceit.com/ru/players/VP_16ssk16/stats/csgo")
urlButton2 = InlineKeyboardButton(text="Ссылка2", url="https://steamcommunity.com/profiles/76561198849309914/")
x = [InlineKeyboardButton(text="Ссылка3", url="https://steamcommunity.com/profiles/76561198849309914/"), InlineKeyboardButton(text="Ссылка4", url="https://steamcommunity.com/profiles/76561198849309914/"), InlineKeyboardButton(text="Ссылка5", url="https://steamcommunity.com/profiles/76561198849309914/")]

urlkb.add(urlButton, urlButton2).row(*x).insert(InlineKeyboardButton(text="Ссылка6", url="https://steamcommunity.com/profiles/76561198849309914/"))

@dp.message_handler(commands="ссылки")
async def url_command(message:types.Message):
    await message.answer("Ссылочки:", reply_markup=urlkb)

inkb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text="Like", callback_data="like_1"), InlineKeyboardButton(text="No Like", callback_data="like_-1"))   

@dp.message_handler(commands="test")
async def test_commands(message:types.Message):
    await message.answer("Проголосуйте", reply_markup=inkb)

@dp.callback_query_handler(Text(startswith="like_"))
async def www_call(callback:types.CallbackQuery):
    result = int(callback.data.split("_")[1])
    if f"{callback.from_user.id}" not in answ:
        answ[f"{callback.from_user.id}"] = result
        await callback.answer("Вы проголосовали")
    else:
        await callback.answer("Вы уже проголосовали", show_alert=True)
  

executor.start_polling(dp, skip_updates=True)    
