from aiogram.utils import executor
from client import dp

async def on_startup(_):
    print('bot is online')

from handlers import client

client.register_handlers_client(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)