from aiogram import types, Dispatcher
from keyboards.client_kb import kb, inline_kb
from random import choice
from uzbek import uzbek
from english import english
from client import bot, dp, storage
from aiogram.types import MediaGroup,InputMediaPhoto
from whatIsLove.main import make_video
from time import sleep
import datetime
import asyncio
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import database




# Calling data from english.py and uzbek.py
uzbek_quotes = uzbek()
english_quotes = english()


# 2 States
class NewTemplate(StatesGroup):
    template_number = State()
    title = State()



@dp.message_handler(commands=['start'])
async def cmd_id(message: types.Message):
    await message.answer(text=f'''{message.from_user.first_name} Eng mashxur iqiboslarini o'qish uchun tilni tanlang''', reply_markup=kb)

    if message.from_user.id not in database.user_number():
        member_id = message.from_user.id
        member_name = message.from_user.full_name
        data = [member_id, member_name]
        try:
            database.add_user(data)
            print(f'New member named [{member_name}] added to the database')

        except:
            print('Failed to add new member to the database')
       
                
    
    # Getting exact time when user started
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    message = f'User[{message.from_user.id}]: Started bot at [{current_time}] \n'

    # write time to file
    with open('log.txt', 'a') as f:
        f.write(message)
        f.close()



# Start point
# @dp.message_handler(commands=['hello'])
async def send_welcome(message: types.Message):
    await message.answer(f'Hello {message.from_user.full_name}')


   
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
    full_name = message.from_user.full_name
    make_video(message.from_user.id, data['title'], data['template_number'])
    await asyncio.sleep(2)
    await message.answer('Video processing...')
    await database.add_template(state, full_name=full_name, user_id=id)
    await state.finish()

    path = f'/home/bahrom/Desktop/TelegramBots/telegram-quotes-bot/whatIsLove/created/{id}.mp4'
    path = open(file=path, mode='rb')
    video = types.InputFile(path)
    msg = '''
    Mike O'Hearn Original Meme Template \n

@bestbekbot
    '''
    await message.reply_video(video=video, caption=msg,reply_markup=kb)


# @dp.message_handler(regexp='(^Video created[s]?$)')
# async def title_saved(message: types.Message):
#     path = f'/home/bahrom/Desktop/Telegram Bots/telegram-quotes-bot/whatIsLove/created/1107759940.mp4'
#     await message.reply_video(video=path, caption='welcome',chat_id=message.from_user.id)


    




def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=['hello'])

