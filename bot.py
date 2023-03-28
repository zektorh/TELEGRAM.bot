import environs
from telebot import TeleBot
from pycoingecko import CoinGeckoAPI

env = environs.Env()

env.read_env('.env')

TOKEN = '5519064364:AAFWHRLYF0NW5J3Wvr68xSfVBvuIW7RC24s'
bot = TeleBot(token= TOKEN)
coin_client = CoinGeckoAPI()


# print(coin_client.get_price(ids= 'bitcoin', vs_currencies= 'usd'))

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام حسن فتاحی هستم ، اسم مورد نظر را تایپ کنید مثل bitcoin")




@bot.message_handler(content_types=['text'])
def cripto_massage_handler(message):
    cripto_id = message.text

    price = coin_client.get_price(ids= cripto_id, vs_currencies= 'usd')

    bot.send_message(chat_id=message.chat.id, text=f"price of {cripto_id} is : {price}")


bot.infinity_polling()