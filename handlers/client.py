from aiogram import types, Dispatcher
from keyboards.client_kb import kb, inline_kb
from random import choice
from uzbek import uzbek
from english import english
from client import bot, dp, storage
from aiogram.types import MediaGroup,InputMediaPhoto
from whatIsLove.main import make_video
from whatIsLove.template_photo import get_photo_list
from time import sleep
import asyncio
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import database as db




uzbek_quotes = uzbek()
english_quotes = english()


class NewTemplate(StatesGroup):
    template_number = State()
    title = State()



# # Start point
# async def start(message: types.Message):
#     await db.db_start(message.from_user.id)

#     await message.reply(f"{message.from_user.first_name} Eng mashxur iqiboslarini o'qish uchun tilni tanlang", reply_markup=kb)



async def send_welcome(message: types.Message):
    if str(message.from_user.id) in db.user_number():
        print('This is old user')
    else:
        member_id = message.from_user.id
        member_name = message.from_user.full_name
        data = [member_name,member_id]
        try:
            db.add_user(data)
            print('New member added to the database')
        except:
            pass

    await message.reply(text='Choose Phone Characteristics', reply_markup=kb)



@dp.message_handler(regexp='(^Uz🇺🇿[s]?$)')
async def uz(message: types.Message):
    await message.answer(choice(uzbek_quotes), reply_markup=kb)
    


      


@dp.message_handler(regexp='(^Eng🏴󠁧󠁢󠁥󠁮󠁧󠁿[s]?$)')
async def eng(message: types.Message):
    await message.answer(choice(english_quotes), reply_markup=kb)




@dp.message_handler(regexp="(^Create Mike O'Hearn meme)")
async def create_meme(message: types.Message):
    await NewTemplate.template_number.set()
    path = f'/home/bahrom/Desktop/TelegramBots/telegram-quotes-bot/whatIsLove/uploads/template.jpg'
    path = open(file=path, mode='rb')
    template = types.InputFile(path)
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=template, 
        reply_markup=inline_kb,
        caption='Choose template'
        )
    






@dp.callback_query_handler(state=NewTemplate.template_number)
async def create_template(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['template_number'] = call.data
    await call.message.answer('Please, enter title to create meme')
    await NewTemplate.next()
    await call.answer()


@dp.message_handler(state=NewTemplate.title)
async def add_item_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['title'] = message.text
    id = message.from_user.id
    make_video(message.from_user.id, data['title'], data['template_number'])
    await asyncio.sleep(6)
    await message.answer('Video created')
    await db.add_template(state,message.from_user.id)
    await state.finish()
    path = f'/home/bahrom/Desktop/TelegramBots/telegram-quotes-bot/whatIsLove/created/1107759940.mp4'
    path = open(file=path, mode='rb')
    video = types.InputFile(path)
    await message.reply_video(video=video, caption='welcome')


# @dp.message_handler(regexp='(^Video created[s]?$)')
# async def title_saved(message: types.Message):
#     path = f'/home/bahrom/Desktop/Telegram Bots/telegram-quotes-bot/whatIsLove/created/1107759940.mp4'
#     await message.reply_video(video=path, caption='welcome',chat_id=message.from_user.id)


    




def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=['start'])

