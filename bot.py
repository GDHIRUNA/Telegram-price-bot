import requests
import telebot

BOT_TOKEN = "YOUR_BOT_TOKEN_HERE" # Get from @BotFather on Telegram
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['price'])
def send_price(message):
    try:
        coin = message.text.split()[1].lower()
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"
        data = requests.get(url).json()
        price = data[coin]['usd']
        bot.reply_to(message, f"{coin.upper()} price: ${price}")
    except:
        bot.reply_to(message, "Usage: /price btc")

print("Bot running...")
bot.polling()
