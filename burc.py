from telethon import TelegramClient, events
import requests
from bs4 import BeautifulSoup

# Telegram API bilgilerinizi girin
api_id = 25989627
api_hash = 'dff2250c7620fef64cd17e4355432d82'
bot_token = '6061198850:AAHAVRNvVRNOv81teRsLWwghhbx4FKXUWL8'

# Telegram istemcisini başlat
client = TelegramClient('burc_bot', api_id, api_hash).start(bot_token=bot_token)

# Burç yorumlarını çeken fonksiyon
def get_horoscope(burc):
    url = f'https://www.hurriyet.com.tr/mahmure/astroloji/{burc}-burcu/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    horoscope = soup.find('p', class_='horoscope-text').text.strip()
    return horoscope

# Botun tepki vermesi için ayarlar
@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond('Merhaba! Hangi burç yorumunu öğrenmek istersin?')

@client.on(events.NewMessage(pattern='/burc'))
async def horoscope(event):
    # Komutun ardından gelen ilk kelimeyi burç olarak alır
    burc = event.text.split()[1].lower()
    horoscope = get_horoscope(burc)
    await event.respond(horoscope)

# Botu çalıştır
client.run_until_disconnected()
