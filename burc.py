from selenium import webdriver
import telebot

# Telegram bot token'ınızı buraya girin
bot = telebot.TeleBot("TOKEN")

# Burçlar ve bağlantıları
astrology_links = {
    "koç": "https://www.hurriyet.com.tr/astroloji/rezzan-kiraz/gunluk-burc-yorumlari/koc",
    "boğa": "https://www.hurriyet.com.tr/astroloji/rezzan-kiraz/gunluk-burc-yorumlari/boga",
    "ikizler": "https://www.hurriyet.com.tr/astroloji/rezzan-kiraz/gunluk-burc-yorumlari/ikizler",
    "yengeç": "https://www.hurriyet.com.tr/astroloji/rezzan-kiraz/gunluk-burc-yorumlari/yengec",
    "aslan": "https://www.hurriyet.com.tr/astroloji/rezzan-kiraz/gunluk-burc-yorumlari/aslan",
    "başak": "https://www.hurriyet.com.tr/astroloji/rezzan-kiraz/gunluk-burc-yorumlari/basak",
    "terazi": "https://www.hurriyet.com.tr/astroloji/rezzan-kiraz/gunluk-burc-yorumlari/terazi",
    "akrep": "https://www.hurriyet.com.tr/astroloji/rezzan-kiraz/gunluk-burc-yorumlari/akrep",
    "yay": "https://www.hurriyet.com.tr/astroloji/rezzan-kiraz/gunluk-burc-yorumlari/yay",
    "oğlak": "https://www.hurriyet.com.tr/astroloji/rezzan-kiraz/gunluk-burc-yorumlari/oglak",
    "kova": "https://www.hurriyet.com.tr/astroloji/rezzan-kiraz/gunluk-burc-yorumlari/kova",
    "balık": "https://www.hurriyet.com.tr/astroloji/rezzan-kiraz/gunluk-burc-yorumlari/balik"
}

# Burç yorumlarını alma fonksiyonu
def get_horoscope(burc):
   try:
        # Tarayıcı sürücüsünü başlatın
        driver = webdriver.Chrome()
        driver.get(astrology_links[burc])

        # Burç yorumunu alın ve düzenleyin
        horoscope = driver.find_element_by_class_name("horoscope-detail").text.strip()

        # Tarayıcı sürücüsünü kapatın
        driver.quit()

        return horoscope
    except:
        return "Burç yorumu alınamadı."

# /start komutu için işlev
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Merhaba! Günlük burç yorumlarını almak için burcunuzu yazın.")

# Burç isimlerine göre yanıt verme işlevi
@bot.message_handler(func=lambda message: True)
def send_horoscope(message):
    burc = message.text.lower()

    if burc in astrology_links.keys():
        horoscope = get_horoscope(burc)
        bot.reply_to(message, horoscope)
    else:
        bot.reply_to(message, "Geçersiz burç adı. Lütfen tekrar deneyin.")

# Botu çalıştırın
bot.polling()


# kodları kendi Telegram botunuzda çalıştırarak, kullanıcılardan aldığınız burç isimlerine göre, Hurriyet Astroloji sayfasından günlük burç yorumlarını alabilirsiniz. Ancak, bu kodu çalıştırmadan önce `TOKEN` yerine kendi Telegram bot token'ınızı girmeniz ve ayrıca `webdriver.Chrome()` yerine kullandığınız tarayıcının sürücüsüne göre değiştirmeniz gerekiyor.
