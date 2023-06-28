from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb = ReplyKeyboardMarkup(resize_keyboard=True)

b1 = KeyboardButton('Uz🇺🇿')
b2 = KeyboardButton('Eng🏴󠁧󠁢󠁥󠁮󠁧󠁿')

kb.add(b1).add(b2)


