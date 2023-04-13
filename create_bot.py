from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

TOKEN = "5967754632:AAFZP5tiAjcHjbyHt-C484E1T-WvBC1xbLc"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)
