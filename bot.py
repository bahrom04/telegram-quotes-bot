from aiogram.utils import executor
from client import dp
from database import connect_db

async def on_startup(_):
    print('bot is online')
    connect_db()
    

from handlers import client

client.register_handlers_client(dp)

if __name__ == '__main__':

    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)