from aiogram import types, Dispatcher
from keyboards import kb
from random import choice
from uzbek import uzbek
from english import english
from client import bot, dp

uzbek_quotes = uzbek()
english_quotes = english()


async def start(message: types.Message):
    await message.reply(f"{message.from_user.first_name} Eng mashxur iqiboslarini o'qish uchun tilni tanlang", reply_markup=kb)

@dp.message_handler(regexp='(^Uz🇺🇿[s]?$)')
async def uz(message: types.Message):
    await message.answer(choice(uzbek_quotes), reply_markup=kb)

@dp.message_handler(regexp='(^Eng🏴󠁧󠁢󠁥󠁮󠁧󠁿[s]?$)')
async def eng(message: types.Message):
    await message.answer(choice(english_quotes), reply_markup=kb)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])

