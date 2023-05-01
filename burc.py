from telethon.sync import TelegramClient
from telethon import events
import requests
from bs4 import BeautifulSoup

api_id = YOUR_API_ID
api_hash = 'YOUR_API_HASH'
client = TelegramClient('session_name', api_id, api_hash)

# Burçlar
burclar = {
    'Kova': 'aquarius',
    'Balık': 'pisces',
    'Koç': 'aries',
    'Boğa': 'taurus',
    'İkizler': 'gemini',
    'Yengeç': 'cancer',
    'Aslan': 'leo',
    'Başak': 'virgo',
    'Terazi': 'libra',
    'Akrep': 'scorpio',
    'Yay': 'sagittarius',
    'Oğlak': 'capricorn'
}

# Günlük burç yorumları
def get_gunluk_burc_yorumu(burc):
    url = f'https://www.hurriyet.com.tr/mahmure/astroloji/{burclar[burc]}-burcu'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    yorum = soup.find('div', {'class': 'lead'}).text.strip()
    return yorum

# Komut işleme
@client.on(events.NewMessage(pattern='/burc'))
async def handle_message(event):
    # Komut parametreleri alınır
    param = event.raw_text.split(' ')[1].capitalize()
    # Geçerli bir burç ise günlük yorumu alınır
    if param in burclar.keys():
        yorum = get_gunluk_burc_yorumu(param)
        await event.respond(f'{param} burcu günlük yorumu:\n\n{yorum}')
    else:
        await event.respond('Geçerli bir burç giriniz.')

client.start()
client.run_until_disconnected()
