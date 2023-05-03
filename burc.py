
import requests
from bs4 import BeautifulSoup

# Telegram bot için gerekli kütüphaneler
import telegram
from telegram.ext import Updater, CommandHandler

# Telegram botunuzun token'ını girin
bot_token = '6061198850:AAHAVRNvVRNOv81teRsLWwghhbx4FKXUWL8'

# Botunuzun işleyeceği komutu belirleyin
def burc_yorumu(update, context):
    # Kullanıcının gönderdiği burç adını alın
    burc = context.args[0].lower()
    
    # Mynet Kadın web sitesindeki burç yorumlarını çekin
    url = f'https://www.mynet.com/kadin/burclar-astroloji/{burc}-burcu-gunluk-yorumu.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    yorumlar = soup.find_all('p', {'class': 'yorum'})
    
    # Kullanıcıya burç yorumunu gönderin
    if len(yorumlar) > 0:
        yorum = yorumlar[0].get_text()
        context.bot.send_message(chat_id=update.effective_chat.id, text=f'{burc.capitalize()} burcu günlük yorumu:\n\n{yorum}')
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text='Hata: Bu burç için yorum bulunamadı.')

# Telegram botunuzu başlatın
updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher

# Botunuzun işleyeceği komutu belirleyin
burc_yorumu_handler = CommandHandler('burcyorumu', burc_yorumu)
dispatcher.add_handler(burc_yorumu_handler)

# Botunuzu çalıştırın
updater.start_polling()
