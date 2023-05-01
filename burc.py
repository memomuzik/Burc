from telethon import TelegramClient, events
import requests
from bs4 import BeautifulSoup

# Telegram API bilgilerinizi girin
api_id = 25989627
api_hash = 'dff2250c7620fef64cd17e4355432d82'
bot_token = '6061198850:AAHAVRNvVRNOv81teRsLWwghhbx4FKXUWL8'

bot = TelegramClient('bot', api_id, api_hash).start(bot_token=TOKEN)


@bot.on(events.NewMessage(pattern='/horo'))
async def horo(event):
    url = 'https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign={}'
    sign = event.message.text.split()[1]

    if sign == 'aries':
        sign = 'Aries'
    elif sign == 'taurus':
        sign = 'Taurus'
    elif sign == 'gemini':
        sign = 'Gemini'
    elif sign == 'cancer':
        sign = 'Cancer'
    elif sign == 'leo':
        sign = 'Leo'
    elif sign == 'virgo':
        sign = 'Virgo'
    elif sign == 'libra':
        sign = 'Libra'
    elif sign == 'scorpio':
        sign = 'Scorpio'
    elif sign == 'sagittarius':
        sign = 'Sagittarius'
    elif sign == 'capricorn':
        sign = 'Capricorn'
    elif sign == 'aquarius':
        sign = 'Aquarius'
    elif sign == 'pisces':
        sign = 'Pisces'
    else:
        return

    res = requests.get(url.format(sign.lower()))
    soup = BeautifulSoup(res.content, 'html.parser')
    horo = soup.find_all('div', {'class': 'block-horoscope-text f16 l20'})
    horoscope = horo[0].find_all('p')
    message = ''
    for hor in horoscope:
        message += hor.text
        message += '\n\n'
    await event.respond('Here is your horoscope for today, {}:\n\n{}'.format(sign.capitalize(), message))


if name == 'main':
    bot.run_until_disconnected()
