from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
from Adafruit_IO import Client,Feed,Data
import os

ADAFRUIT_IO_USERNAME = os.getenv('ADAFRUIT_IO_USERNAME')
ADAFRUIT_IO_KEY = os.getenv('ADAFRUIT_IO_KEY')
aio = Client('ADAFRUIT_IO_USERNAME','ADAFRUIT_IO_KEY')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

def start(bot, update):
    print(str( update.effective_chat.id ))
    bot.send_message(chat_id = update.effective_chat.id, text="Welcome! Type 'Turn on the Light' or /lighton to switch on the light bulb. Type 'Turn off the Light' or /lightoff to switch off the light bulb.")

def unknown(bot, update):
    bot.send_message(chat_id=update.effective_chat.id, text="Oops, I didn't understand that. Try again!")


def value_send(value):
  to_feed = aio.feeds('lightbotctrl')
  aio.send_data(to_feed.key,value)

def lighton(bot, update):
  chat_id = update.message.chat_id
  bot.send_message(chat_id, text="Light has been turned ON")
  bot.send_photo(chat_id, photo='https://www.securityroundtable.org/wp-content/uploads/2019/03/AdobeStock_261504199-scaled.jpeg')
  value_send(1)

def lightoff(bot, update):
  chat_id = update.message.chat_id
  bot.send_message(chat_id, text="Light has been turned OFF")
  bot.send_photo(chat_id=update.effective_chat.id,photo='https://ak.picdn.net/shutterstock/videos/1027638404/thumb/1.jpg?ip=x480')
  value_send(0)

def given_message(bot, update):
  text = update.message.text.upper()
  text = update.message.text
  if text == 'Turn on the Light':
    lighton(bot,update)
  
  elif text == 'Turn off the Light':
    lightoff(bot,update)

u = Updater('TELEGRAM_TOKEN',use_context = True)
dp = u.dispatcher
dp.add_handler(CommandHandler('lighton',lighton))
dp.add_handler(CommandHandler('lightoff',lightoff))
dp.add_handler(CommandHandler('start', start))
dp.add_handler(MessageHandler(Filters.command, unknown))
dp.add_handler(MessageHandler(Filters.text, given_message))

u.start_polling()
u.idle()
