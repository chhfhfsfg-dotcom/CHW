import telebot

TOKEN = "8910504804:AAHXbQ7SZy1rK41sw4ckEqBLAhWCl1LSNZE"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك! تم تشغيل البوت بنجاح.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"وصلت رسالتك: {message.text}")

bot.polling()
