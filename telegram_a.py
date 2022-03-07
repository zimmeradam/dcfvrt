import telegram

bot_token = '1252496943:AAH0L5rIaQOc6sCw7E23s0nUgrlQsOih8iw'
bot = telegram.Bot(token=bot_token)

def sendMsg(msg, bot_chatID):
    bot.sendMessage(chat_id=bot_chatID, text=msg)

