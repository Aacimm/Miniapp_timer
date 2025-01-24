from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "7851178513:AAHDfs2Jtd3ld6zheQ1je64KwjXDRYk9izk"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Кнопка для открытия вашего сайта
    keyboard = [
        [InlineKeyboardButton("Посмотреть результаты событий", web_app={"url": "https://results.russiarunning.com/"})]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Отправляем сообщение с кнопкой
    await update.message.reply_text("Нажмите кнопку ниже, чтобы открыть сайт:", reply_markup=reply_markup)

if __name__ == "__main__":
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()