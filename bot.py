from telegram import *
from telegram.ext import *

TOKEN = "8708223198:AAFsn_gOErFw7A9QilhGiMJLXOy12UbgUlA"

def start(update, context):
    keyboard = [[InlineKeyboardButton("Satın Al ⭐", callback_data='buy')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("🚀 Programı satın almak için tıkla:", reply_markup=reply_markup)

def button(update, context):
    query = update.callback_query
    query.answer()

    if query.data == 'buy':
        context.bot.send_invoice(
            chat_id=query.message.chat_id,
            title="Premium Program",
            description="Full erişim program",
            payload="program",
            provider_token="",
            currency="XTR",
            prices=[LabeledPrice("Program", 100)]
        )

def successful_payment(update, context):
    update.message.reply_text(
        "✅ Ödeme başarılı!\n\nİndirme linkin:\https://t.me/+LYBKD7SlsgpjY2Jk"
    )

updater = Updater(TOKEN)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(CallbackQueryHandler(button))
dp.add_handler(MessageHandler(Filters.successful_payment, successful_payment))

updater.start_polling()
updater.idle()
