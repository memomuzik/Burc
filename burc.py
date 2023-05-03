import requests
from bs4 import BeautifulSoup
from telethon.sync import TelegramClient

# Telegram botu API anahtarları
api_id = '25989627'
api_hash = 'dff2250c7620fef64cd17e4355432d82'
bot_token = '6061198850:AAHAVRNvVRNOv81teRsLWwghhbx4FKXUWL8'
channel_username = 'burcyorumkanal'

# İnternet sitesinden metni alın ve işleyin
url = 'https://www.mynet.com/kadin/burclar-astroloji/koc-burcu-gunluk-yorumu.html'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
text = soup.get_text()

# Telethon ile Telegram botunu başlatın
client = TelegramClient('session_name', api_id, api_hash).start(bot_token=bot_token)

# Metni Telegram kanalına gönderin
client.send_message(channel_username, text)

client.run_until_disconnected()
