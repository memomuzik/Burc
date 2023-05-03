from telethon import TelegramClient, events
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
# Telegram API bilgilerinizi girin
api_id = 25989627
api_hash = 'dff2250c7620fef64cd17e4355432d82'
bot_token = '6061198850:AAHAVRNvVRNOv81teRsLWwghhbx4FKXUWL8'

client = TelegramClient('burcbot', api_id, api_hash).start(bot_token=bot_token)

browser = webdriver.Chrome() # Chrome tarayıcısını aç
browser.get("https://www.mynet.com/kadin/burclar-astroloji")
burc_yorumlari = browser.find_elements(By.XPATH, "//div[contains(@class, 'tab-panel')]") # Burç yorumlarını al
browser.close() # Tarayıcıyı kapat


# Bot başlatıldığında /start komutuyla karşılama mesajı gönder
@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond('Merhaba, ben burc yorum botu! Bugünün burç yorumları şunlar:\n\n')


# Burç yorumlarını kullanıcıya göster
@client.on(events.NewMessage(pattern='/yorumlar'))
async def yorumlar(event):
    for yorum in burc_yorumlari:
        burc_adlari = yorum.find_elements(By.XPATH, "//a[contains(@class, 'tab-label')]")
        burc_yorumu = yorum.find_element(By.XPATH, "//p[not(@class)]")
        msg = f"{burc_adlari[0].text} burcu:\n{burc_yorumu.text}\n\n"
        await event.respond(msg)

# Botu çalıştır
client.run_until_disconnected()
