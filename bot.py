from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, LabeledPrice
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    PreCheckoutQueryHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = "8795137194:AAHt_D42S2SZ6nbdlmBilUVLGY8DEoGaIuc"

DOWNLOAD_LINK = "https://t.me/+x8Vw2rdnTi81YzQ0"
PRICE_STARS = 2500

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("Satın Al ⭐", callback_data="buy")]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🚀 Programı satın almak için tıkla:\n\n"
        f"⭐ Fiyat: {PRICE_STARS} Stars",
        reply_markup=reply_markup
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "buy":
        await context.bot.send_invoice(
            chat_id=query.message.chat_id,
            title="Pasha Yazılım Programı",
            description="Ödeme sonrası indirme linki otomatik gönderilir.",
            payload="pasha_program_2500_stars",
            provider_token="",
            currency="XTR",
            prices=[LabeledPrice("Program", PRICE_STARS)]
        )

async def precheckout(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.pre_checkout_query
    await query.answer(ok=True)

async def successful_payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ Ödeme başarılı!\n\n"
        "📥 İndirme / erişim linkin:\n"
        f"{DOWNLOAD_LINK}\n\n"
        "Teşekkürler!"
    )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))
app.add_handler(PreCheckoutQueryHandler(precheckout))
app.add_handler(MessageHandler(filters.SUCCESSFUL_PAYMENT, successful_payment))

app.run_polling()
