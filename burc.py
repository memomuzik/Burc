from telethon import TelegramClient, events
import requests
from bs4 import BeautifulSoup

# Telegram API bilgilerinizi girin
api_id = 25989627
api_hash = 'dff2250c7620fef64cd17e4355432d82'
bot_token = '6061198850:AAHAVRNvVRNOv81teRsLWwghhbx4FKXUWL8'

client = TelegramClient('burcyorum', api_id, api_hash).start(bot_token=bot_token)


# Burç yorumu çeken fonksiyon
def get_horoscope(burc):
    url = 'https://www.elle.com.tr/astroloji/gunluk-burc-yorumlari'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    horoscopes = soup.find('div', {'class': 'section daily-horoscope'})
    burc_dict = {
        'koç': 'aries',
        'boğa': 'taurus',
        'ikizler': 'gemini',
        'yengeç': 'cancer',
        'aslan': 'leo',
        'başak': 'virgo',
        'terazi': 'libra',
        'akrep': 'scorpio',
        'yay': 'sagittarius',
        'oglak': 'capricorn',
        'kova': 'aquarius',
        'balık': 'pisces'
    }
    try:
        horoscope = horoscopes.find('div', {'class': burc_dict[burc]}).text.strip()
    except:
        horoscope = 'Hata oluştu'
    return horoscope

# Telegram event handler
@client.on(events.NewMessage(pattern='/burcyorumu'))
async def handle(event):
    message = event.message.message
    burc = message.split(' ')[1] # örn. /burcyorumu aslan
    horoscope = get_horoscope(burc)
    await event.respond(f'{burc.capitalize()} burcu günlük yorumu:\n{horoscope}')

# İstemci başlatma
client.start()
client.run_until_disconnected()
