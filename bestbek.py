from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes,ConversationHandler,MessageHandler,filters
from random import choice
from uzbek import uzbek
from english import english

uzbek_quotes = uzbek()
english_quotes = english()


buttons = ReplyKeyboardMarkup([['Uzbek'], ['English']], resize_keyboard=True)

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        f"Assalomu alaykum {update.effective_user.first_name}\nEng mashxur iqiboslarini o'qish uchun tilni tanlang", reply_markup=buttons)
    return 1

async def uzbek(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(choice(uzbek_quotes))

async def english(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(choice(english_quotes))


app = ApplicationBuilder().token("6298564597:AAFxPkJyCIajSKrZHhg8Hm7lv4M2qzzwguY").build()

conversation_handler = ConversationHandler(
    entry_points = [CommandHandler('hello', hello)],
    states= {
        1:[
            MessageHandler(filters.Regex('^(Uzbek)$'), uzbek),
            MessageHandler(filters.Regex('^(English)$'), english)
        ]
    },
    fallbacks=[MessageHandler(filters.TEXT, hello)]
)
app.add_handler(conversation_handler)

app.run_polling()
