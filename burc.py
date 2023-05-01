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
    response = requests.get(f'https://www.mynet.com/kadin/burclar-astroloji/{burc}-burcu-gunluk-yorumu')
    soup = BeautifulSoup(response.content, 'html.parser')
    horoscope_text = soup.find('p', class_='horoscope-text')
    if horoscope_text:
        horoscope = horoscope_text.text.strip()
        return horoscope
    else:
        return f'{burc.capitalize()} burcu için yorum bulunamadı.'

# Botun tepki vermesi için ayarlar
@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond('Merhaba! Hangi burç yorumunu öğrenmek istersin?')

@client.on(events.NewMessage(pattern='/burc'))
async def horoscope(event):
    # Komutun ardından gelen kelime sayısı 2'den az ise hata mesajı gönder
    if len(event.text.split()) < 2:
        await event.respond('Lütfen bir burç adı girin.')
        return
    # Komutun ardından gelen ilk kelimeyi burç olarak alır
    burc = event.text.split()[1].lower()
    horoscope = get_horoscope(burc)
    await event.respond(horoscope)
# Botu çalıştır
client.run_until_disconnected()
