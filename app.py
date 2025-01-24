from flask import Flask, render_template, request
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup

app = Flask(__name__)

# Telegram Bot Token
BOT_TOKEN = '7241854328:AAEIeZYqcB3n58GGJGCnn4wkXWBD0u5C5dE'
bot = Bot(token=BOT_TOKEN)

@app.route('/')
def index():
    return render_template('index.html')  # Интерфейс таймера

@app.route('/notify', methods=['POST'])
def notify():
    # Получаем ID чата и сообщение о завершении
    chat_id = request.form.get('chat_id')
    message = request.form.get('message', 'Время вышло!')
    bot.send_message(chat_id=chat_id, text=message)
    return "Уведомление отправлено", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)