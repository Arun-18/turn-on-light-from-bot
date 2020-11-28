!pip install adafruit-io
x = "Kumar13"  #ADAFRUIT_IO_USERNAME
y = "aio_UHZA63kUi0x1anfYfeJwWG9gQ82w" #ADAFRUIT_IO_KEY
from Adafruit_IO import Client, Feed
aio = Client(x,y)
# create feed
feed=Feed(name='bot118') # Feed name is given
result = aio.create_feed(feed)
result
from Adafruit_IO import Data
#sending a value to a feed
value=Data(value=0) 
value_send=aio.create_data('bot',value)
# Telegram API
# 1.create telegram bot
# 2.send a query
!pip install python-telegram-bot
from telegram.ext import Updater,CommandHandler
import requests #getting data from the cloud

def get_url():
    contents=requests.get('https://random.dog/woof.json').json()
    url=contents['url']
    return url

def dog(bot,update):
    url=get_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id,photo=url)

u = Updater('1400818256:AAHC211LcAFE2wd2JaRS1AVzRv7x_i9unZ8')
dp = u.dispatcher
dp.add_handler(CommandHandler('dog',dog))
u.start_polling()
u.idle()
