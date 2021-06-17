# from telegram.ext import Updater
from credentials.info import bot_token, bot_user_name, api_id, api_hash

# bot = telegram.Bot(token=bot_token)
# updater = Updater(token='TOKEN', use_context=True)
# dispatcher = updater.dispatcher
# import logging
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                      level=logging.INFO)
# def start(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

# from telegram.ext import CommandHandler
# start_handler = CommandHandler('start', start)
# dispatcher.add_handler(start_handler)

import telebot
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient, sync, events

bot_token
message = "Working..."
phone = '+601121347732'


client = TelegramClient('session', api_id, api_hash)
client.connect()
client.sign_in(phone, 19399)

# client.send_message('+60173526903', 'Am I speaking to Candice?')
