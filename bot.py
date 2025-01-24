from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = '7241854328:AAEIeZYqcB3n58GGJGCnn4wkXWBD0u5C5dE'


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Открыть Таймер", web_app={"url": "https://miniapp-timer.onrender.com"})]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Запусти таймер!", reply_markup=reply_markup)


if __name__ == '__main__':
    # Инициализация приложения телеграм 1
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Добавление обработчика команды /start
    application.add_handler(CommandHandler('start', start))

    # Запуск бота
    application.run_polling()