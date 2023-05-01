import asyncio
import logging
import os
import random

from telethon import TelegramClient, events
from bs4 import BeautifulSoup
import requests


# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Set up environment variables
api_id = int(os.environ.get('25989627'))
api_hash = os.environ.get('dff2250c7620fef64cd17e4355432d82')
bot_token = os.environ.get('6061198850:AAHAVRNvVRNOv81teRsLWwghhbx4FKXUWL8')
channel_username = os.environ.get('burcyorumvefa')


# Set up Telegram client
client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)


# Get daily horoscope
def get_horoscope(sign):
    url = f'https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-{sign.lower()}.aspx'
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    horoscope = soup.find('div', {'class': 'main-horoscope'}).p.text.strip()
    return horoscope


# Handle "/start" command
@client.on(events.NewMessage(pattern='/start'))
async def handle_start(event):
    await event.respond("Hi! I'm your daily horoscope bot. What's your zodiac sign? (e.g. /horoscope Aries)")
    raise events.StopPropagation


# Handle "/horoscope" command
@client.on(events.NewMessage(pattern='/horoscope\s+(\w+)'))
async def handle_horoscope(event):
    sign = event.pattern_match.group(1)
    horoscope = get_horoscope(sign)
    await client.send_message(event.chat_id, f"Here's your daily horoscope for {sign}: \n\n{horoscope}")


# Start the client
async def main():
    await client.send_message(channel_username, 'Bot is now online!')
    await client.run_until_disconnected()


if __name__ == '__main__':
    logger.info('Starting bot...')
    asyncio.run(main())
```

In this example code, you need to set up the environment variables `API_ID`, `API_HASH`, `BOT_TOKEN`, and `CHANNEL_USERNAME` with your own values. You can obtain the `API_ID` and `API_HASH` by creating a new application on the Telegram website. `BOT_TOKEN` can be obtained by creating a new bot through BotFather. `CHANNEL_USERNAME` is the username of the Telegram channel where you want to receive notification about the bot online status.

Once you have set up the environment variables, you can run the script and interact with the bot by sending commands to it. For example, you can send `/start` to the bot to initialize it, and then send `/horoscope Aries` to get the daily horoscope for the Aries zodiac sign.
 
