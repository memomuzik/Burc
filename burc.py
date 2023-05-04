from telethon import TelegramClient, events
import requests
from bs4 import BeautifulSoup
import datetime
import random
api_id = '25989627'
api_hash = 'dff2250c7620fef64cd17e4355432d82'
bot_token = '6061198850:AAHAVRNvVRNOv81teRsLWwghhbx4FKXUWL8'

bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond('Merhaba, burç yorumlarına hoş geldiniz! Lütfen burcunuzu seçin: \nKoç ♈️\nBoğa ♉️\nİkizler ♊️\nYengeç ♋️\nAslan ♌️\nBaşak ♍️\nTerazi ♎️\nAkrep ♏️\nYay ♐️\nOğlak ♑️\nKova ♒️\nBalık ♓️')

@bot.on(events.NewMessage(pattern='/koç'))
async def koç(event):
    await event.respond('Burcunuz Koç ♈️\n\n' + get_horoscope('koç'))

@bot.on(events.NewMessage(pattern='/boğa'))
async def boğa(event):
    await event.respond('Burcunuz Boğa ♉️\n\n' + get_horoscope('boğa'))

@bot.on(events.NewMessage(pattern='/ikizler'))
async def ikizler(event):
    await event.respond('Burcunuz İkizler ♊️\n\n' + get_horoscope('ikizler'))

@bot.on(events.NewMessage(pattern='/yengeç'))
async def yengeç(event):
    await event.respond('Burcunuz Yengeç ♋️\n\n' + get_horoscope('yengeç'))

@bot.on(events.NewMessage(pattern='/aslan'))
async def aslan(event):
    await event.respond('Burcunuz Aslan ♌️\n\n' + get_horoscope('aslan'))

@bot.on(events.NewMessage(pattern='/başak'))
async def başak(event):
    await event.respond('Burcunuz Başak ♍️\n\n' + get_horoscope('başak'))

@bot.on(events.NewMessage(pattern='/terazi'))
async def terazi(event):
    await event.respond('Burcunuz Terazi ♎️\n\n' + get_horoscope('terazi'))

@bot.on(events.NewMessage(pattern='/akrep'))
async def akrep(event):
    await event.respond('Burcunuz Akrep ♏️\n\n' + get_horoscope('akrep'))

@bot.on(events.NewMessage(pattern='/yay'))
async def yay(event):
    await event.respond('Burcunuz Yay ♐️\n\n' + get_horoscope('yay'))

@bot.on(events.NewMessage(pattern='/oğlak'))
async def oğlak(event):
    await event.respond('Burcunuz Oğlak ♑️\n\n' + get_horoscope('oğlak'))

@bot.on(events.NewMessage(pattern='/kova'))
async def kova(event):
    await event.respond('Burcunuz Kova ♒️\n\n' + get_horoscope('kova'))

@bot.on(events.NewMessage(pattern='/balık'))
async def balık(event):
    await event.respond('Burcunuz Balık ♓️\n\n' + get_horoscope('balık'))

def get_horoscope(burc):
    url = 'https://www.mynet.com/kadin/burclar-astroloji/' + burc + '-burcu-gunluk-yorumu.html'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    horoscope = soup.find(class_='detail-content-box')
    date = datetime.date.today().strftime('%d.%m.%Y')
    horoscope_text = horoscope.get_text()
    message_lines = horoscope_text.split('\n')
    selected_lines = message_lines[100:110]
    selected_text = '\n'.join(selected_lines)
    return f'{date} tarihli {burc.capitalize()} burcu yorumu:\n\n{selected_text}'
   # return f'{date} tarihli {burc.capitalize()} burcu yorumu:\n\n{horoscope.get_text()}'


@bot.on(events.NewMessage(pattern="/etiketle"))
async def etiketle(event):
    chat = await event.get_chat()
    users = await bot.get_participants(chat)
    mention1 = random.choice(users).mention
    mention2 = random.choice(users).mention
    await bot.send_message(chat, f"{mention1} ve {mention2}, artık arkadaşsınız.")

bot.run_until_disconnected()
