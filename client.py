from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
bot = Bot(token='6094429458:AAHqt5UjgoSYXvO8vCzRAKpJ4vUj3I94FqY')
dp = Dispatcher(bot, storage=storage)




