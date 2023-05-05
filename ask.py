from telethon import TelegramClient, events
import requests
from bs4 import BeautifulSoup
import datetime
import random

@bot.on(events.NewMessage(pattern="/ask"))
async def ask(event):
    chat = await event.get_chat()
    users = await bot.get_participants(chat) 
    mention1 = random.choice(users).username
    mention2 = random.choice(users).username
    await bot.send_message(chat, f"Ve işte beklenen oldu😯😯😯\n\n@{mention1} ❤️ @{mention2}\n\naşkın oku kalplerine saplandı.🏹💘")

