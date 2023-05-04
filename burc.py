from telethon import TelegramClient, events
import requests
from bs4 import BeautifulSoup
import datetime
import random
from telethon.errors import SessionPasswordNeededError
api_id = '25989627'
api_hash = 'dff2250c7620fef64cd17e4355432d82'
bot_token = '6061198850:AAHAVRNvVRNOv81teRsLWwghhbx4FKXUWL8'

bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond('Merhaba, burç yorumlarına hoş geldiniz! Lütfen burcunuzu başına / koyarak yazın ve yorumunuz gelsin\n\nNot: Yoğunluk nedeniyle ve verilen kota nedeniyle burcunuz görüntülenemeyebilir bir süre sonra tekrar deneyiniz veya yardım için: @yoodelidegilim \n\n\nAyrıca aşk okunu kullanmak isterseniz /ask komutunu kullanabilirsiniz🏹💘')

@bot.on(events.NewMessage(pattern='/koc'))
async def koc(event):
    await event.respond('Burcunuz Koç ♈️\n\n' + get_horoscope('koc'))

@bot.on(events.NewMessage(pattern='/boga'))
async def boga(event):
    await event.respond('Burcunuz Boğa ♉️\n\n' + get_horoscope('boga'))

@bot.on(events.NewMessage(pattern='/ikizler'))
async def ikizler(event):
    await event.respond('Burcunuz İkizler ♊️\n\n' + get_horoscope('ikizler'))

@bot.on(events.NewMessage(pattern='/yengec'))
async def yengec(event):
    await event.respond('Burcunuz Yengeç ♋️\n\n' + get_horoscope('yengec'))

@bot.on(events.NewMessage(pattern='/aslan'))
async def aslan(event):
    await event.respond('Burcunuz Aslan ♌️\n\n' + get_horoscope('aslan'))

@bot.on(events.NewMessage(pattern='/basak'))
async def basak(event):
    await event.respond('Burcunuz Başak ♍️\n\n' + get_horoscope('basak'))

@bot.on(events.NewMessage(pattern='/terazi'))
async def terazi(event):
    await event.respond('Burcunuz Terazi ♎️\n\n' + get_horoscope('terazi'))

@bot.on(events.NewMessage(pattern='/akrep'))
async def akrep(event):
    await event.respond('Burcunuz Akrep ♏️\n\n' + get_horoscope('akrep'))

@bot.on(events.NewMessage(pattern='/yay'))
async def yay(event):
    await event.respond('Burcunuz Yay ♐️\n\n' + get_horoscope('yay'))

@bot.on(events.NewMessage(pattern='/oglak'))
async def oglak(event):
    await event.respond('Burcunuz Oğlak ♑️\n\n' + get_horoscope('oglak'))

@bot.on(events.NewMessage(pattern='/kova'))
async def kova(event):
    await event.respond('Burcunuz Kova ♒️\n\n' + get_horoscope('kova'))

@bot.on(events.NewMessage(pattern='/balik'))
async def balik(event):
    await event.respond('Burcunuz Balık ♓️\n\n' + get_horoscope('balik'))

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


@bot.on(events.NewMessage(pattern="/ask"))
async def ask(event):
    chat = await event.get_chat()
    users = await bot.get_participants(chat) 
    mention1 = random.choice(users).username
    mention2 = random.choice(users).username
    await bot.send_message(chat, f"Ve işte beklenen oldu😯😯😯\n\n@{mention1} ❤️ @{mention2}\n\naşkın oku kalplerine saplandı.🏹💘")


@bot.on(events.NewMessage(pattern='/sayi'))
async def baslat(event):
    baslatan = await event.get_sender()
    eti = f"[{baslatan.first_name}](tg://user?id={baslatan.id})" # Kişiyi Etikete Dönüştürelim
    await event.respond(f'Sanırım Kendine Güveniyorsun {eti}\n\n● 1 İle 1000 Arasında Bir Sayı Tuttum Lütfen Tahminilerini Yaz\nBen Seni Yönlendireceğim!')


    tutulan = random.randint(1, 1000)
    sayac = 0


# Tahminleri Alalım
    @bot.on(events.NewMessage)
    async def tahmin_al(event):
        username = f'[{event.sender.first_name}](tg://user?id={event.sender.id})'
        nonlocal sayac # Sayacımızı Sayı İçeren Mesajları Saymak İçin Başlatalım
        try:
            tahmin = int(event.message.text)
        except ValueError: # Oyun Aktifken Gelen Mesajların Sayı Olmadığında Duralım Ve Sessiz Bir Şekilde Hata Verelim Ama Hatayı Dışarıya Yansıtmayalım
            return # Gelen Mesaj Sayı İçeriyor ise Devam Edelim

        sayac += 1 # Tahmin Sayacı Her Sayı İçeren Mesaj Geldiğinde Bir Tahmin Sayısı Ekleyelim

        if tahmin == tutulan: # Gelen Mesaj Tutulan Sayı İle Eşleşiyorsa Tebrik Edelim
            await event.respond(f'{username} 💐 Tebrikler!\n\n➥ {tahmin} Sayısını Bildiniz\n\n● Sayıyı Bilmek İçin {sayac} Kere Uğraştınız!')
            bot.remove_event_handler(tahmin_al)
     
         
        elif tahmin < tutulan: # Mesajdaki Sayı Seçilenden Küçük İse Uyarı Verelim
            await event.respond(f'{username} Daha Yüksek Bir Sayı Söyle ⬆️')
        else: # Zıt Tahmin
            await event.respond(f'{username} Daha Düşük Bir Sayı Söyle ⬇️') # Tam Tersini Yapalım


    @bot.on(events.NewMessage(pattern='/tahminbitir'))
    async def stop_game(event):
        await event.respond('Oyun durduruldu.')
        bot.remove_event_handler(tahmin_al)

async def play_hangman(chat_id):
    word_list = ['python', 'telethon', 'bot', 'telegram', 'openai']
    word = random.choice(word_list)
    game = Hangman(chat_id, word)
    await game.start()

await play_hangman(CHAT_ID)

class Hangman:
    def init(self, chat_id, word):
        self.chat_id = chat_id
        self.word = word.lower()
        self.guesses = set()
        self.wrong_guesses = 0

    async def start(self):
        await client.send_message(self.chat_id, 'Adam asmaca oyununa hoş geldiniz!')
        await self.show_guesses()
        await self.play()

    async def play(self):
        while self.wrong_guesses < 6:
            guess = await self.get_guess()
            if guess in self.word:
                self.guesses.add(guess)
                if self.is_won():
                    await self.end('Kazandınız!')
                    return
            else:
                self.wrong_guesses += 1
                if self.is_lost():
                    await self.end('Kaybettiniz! Kelime "{}" idi.'.format(self.word.upper()))
                    return
            await self.show_guesses()

    async def get_guess(self):
        message = await client.send_message(self.chat_id, 'Tahmin etmek istediğiniz harfi veya kelimeyi girin:')
        guess = (await client.get_message(message.to_id, message.id)).message
        if len(guess) == 1:
            return guess.lower()
        else:
            return guess.lower().strip()

    async def show_guesses(self):
        masked_word = ''
        for letter in self.word:
            if letter in self.guesses:
                masked_word += letter
            else:
                masked_word += '_'
        await client.send_message(self.chat_id, masked_word)
        await self.show_hangman()

    async def show_hangman(self):
        hangman = [
            ' _____     ',
            '|         |    ',
            '|         {}    ',
            '|        {}{}{} ',
            '|        {} {}  ',
            '|              ',
            '|              ',
        ]
        if self.wrong_guesses == 0:
            await client.send_message(self.chat_id, '\n'.join(hangman).format('', '', '', '', ''))
        elif self.wrong_guesses == 1:
            await client.send_message(self.chat_id, '\n'.join(hangman).format('O', '', '', '', ''))
        elif self.wrong_guesses == 2:
            await client.send_message(self.chat_id, '\n'.join(hangman).format('O', '', '', '', '|'))
        elif self.wrong_guesses == 3:
            await client.send_message(self.chat_id, '\n'.join(hangman).format('O', '', '', '', '|\\'))
        elif self.wrong_guesses == 4:
            await client.send_message(self.chat_id, '\n'.join(hangman).format('O', '', '', '', '/|\\'))
        elif self.wrong_guesses == 5:
            await client.send_message(self.chat_id, '\n'.join(hangman).format('O', '', '', '', '/|\\'))
        else:
            await client.send_message(self.chat_id, '\n'.join(hangman).format('O', '/', '|', '\\', '/ \\' ))

    def is_won(self):
        for letter in self.word:
            if letter not in self.guesses:
                return False
        return True


    def is_lost(self):
        return self.wrong_guesses == 6

    async def end(self, message):
        await client.send_message(self.chat_id, message)
bot.run_until_disconnected()
