
import telegram
from telegram.ext import Updater, CommandHandler
import asyncio
# Telegram bot token
TOKEN = 'PROVIDE_YOUR_TELEGRAM_BOT_TOKEN_HERE'

# Chat ID of the user to notify
USER_CHAT_ID = 'PROVIDE_YOUR_CHAT_ID_HERE'

# Create a Telegram bot instance
bot = telegram.Bot(token=TOKEN)


async def call():
    suspect = "captured_frame.jpg"
    await bot.send_photo(chat_id=USER_CHAT_ID, photo=open(suspect, 'rb'))
    await bot.send_message(chat_id=USER_CHAT_ID, text='WARNING!!! Intruder Detected in your vehicle.')
    
if __name__ == '__main__':
    asyncio.run(call())
    



