
import telebot
TOKEN = "5943906117:AAGCPsWaznqdenSZbjSMJDZQxBs2Xu-WPeA"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Welcome, my friend! \ c{message.chat.username}")

@bot.message_handler(content_types=['photo'])
def send_photo(message: telebot.types.Message):
    bot.reply_to(message, "Nice!")

bot.polling(none_stop=True)
