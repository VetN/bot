import telebot
TOKEN = "5943906117:AAGCPsWaznqdenSZbjSMJDZQxBs2Xu-WPeA"
bot = telebot.TeleBot(TOKEN)
bot.polling(none_stop=True)


# Обрабатываются все сообщения содержащие команды '/start' or '/help'.
#@bot.message_handler(commands=['start', 'help'])
#def handle_start_help(message):
    #pass


# Обрабатывается все документы и аудиозаписи
#@bot.message_handler(content_types=['document', 'audio'])
#def handle_docs_audio(message):
    #pass

# бот берет из сообщ username и выдает приветст сообщ с привязкой к пользоват
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Welcome, \ c{message.chat.username}")

#  бот на сообщ с фотограф отвечает Nice!
@bot.message_handler(content_types=['photo'])
def send_photo(message: telebot.types.Message):
    bot.reply_to(message, "Nice!")

