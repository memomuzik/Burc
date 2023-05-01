from telethon import TelegramClient, events
import requests
from bs4 import BeautifulSoup

# Telegram API bilgilerinizi girin
api_id = 25989627
api_hash = 'dff2250c7620fef64cd17e4355432d82'
bot_token = '6061198850:AAHAVRNvVRNOv81teRsLWwghhbx4FKXUWL8'

client = TelegramClient('burcbot', api_id, api_hash).start(bot_token=bot_token)

# Burç yorumu çeken fonksiyon
def get_horoscope(burc):
    url = f'https://www.hurriyet.com.tr/mahmure/astroloji/{burc}-burcu/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    horoscope_text = soup.find('div', {'class': 'horoscopetext'})
    if not horoscope_text:
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
            horoscope_text = horoscopes.find('div', {'class': burc_dict[burc]}).text.strip()
        except:
            horoscope_text = 'Hata oluştu'
    else:
        horoscope_text = horoscope_text.text.strip()
    return horoscope_text

# Telegram event handler
@client.on(events.NewMessage(pattern='/burcyorumu'))
async def handle(event):
    message = event.message
    try:
        burc = message.text.split(' ')[1].lower() # örn. /burcyorumu koc
        burc_list = ['koç', 'boğa', 'ikizler', 'yengeç', 'aslan', 'başak', 'terazi', 'akrep', 'yay', 'oglak', 'kova', 'balık']
        if burc in burc_list:
            horoscope = get_horoscope(burc)
            await event.respond(f'{burc.capitalize()} burcu günlük yorumu:\n{horoscope}')
        else:
            await event.respond('Geçersiz burç ismi. Lütfen geçerli bir burç ismi girin.')
    except:
        await event.respond('Geçersiz komut. Lütfen "/burcyorumu <burc>" şeklinde bir komut girin.')

# İstemci başlatma
client.start()
client.run_until_disconnected()
