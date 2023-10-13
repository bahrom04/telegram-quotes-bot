from aiogram.types import (
    KeyboardButton,
    ReplyKeyboardMarkup, 
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('Uz🇺🇿')
b2 = KeyboardButton('Eng🏴󠁧󠁢󠁥󠁮󠁧󠁿')
b3 = KeyboardButton("Create Mike O'Hearn meme")
kb.add(b1).add(b2).add(b3)


inline_kb = InlineKeyboardMarkup(row_width=2)
inline_b1 = InlineKeyboardButton(text='1', callback_data='1')
inline_b2 = InlineKeyboardButton(text='2', callback_data='2')
inline_b3 = InlineKeyboardButton(text='3', callback_data='3')
inline_b4 = InlineKeyboardButton(text='4', callback_data='4')


# buttons = (inline_b1,inline_b2,inline_b3)
inline_kb.add(inline_b1, inline_b2, inline_b3, inline_b4)





