from telethon.sync import TelegramClient
from telethon import events
from bs4 import BeautifulSoup
import requests
api_id = 25989627
api_hash = 'dff2250c7620fef64cd17e4355432d82'
bot_token = '6061198850:AAHAVRNvVRNOv81teRsLWwghhbx4FKXUWL8'
client = TelegramClient('burcbot', api_id, api_hash).start(bot_token=bot_token)

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
    url = f'https://www.hurriyet.com.tr/gunluk-burc-yorumlari/{burc}-burcu/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    yorum_div = soup.find('div', {'class': 'lead'})
    if yorum_div is None:
        raise ValueError('Günlük burç yorumu bulunamadı.')
    yorum = yorum_div.text.strip()
    return yorum

# Komut işleme
@client.on(events.NewMessage(pattern='/burc'))
async def burc(event):
    try:
        command, param = event.raw_text.split(' ')
        if command.lower() == '/burc':
            yorum = get_gunluk_burc_yorumu(param)
            await event.respond(yorum)
    except ValueError as e:
        await event.respond(str(e))
    except:
        await event.respond('Bir hata oluştu.')
client.start()
client.run_until_disconnected()
