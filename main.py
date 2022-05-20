# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import telebot
from telebot import types
bot = telebot.TeleBot("5090925332:AAG4vpXt2N65Ucdz4xaHM7eKXgg2mN2gfqE", parse_mode=None)

from parsing import Parser, check_time, get_local_photo
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
@bot.message_handler(commands=['start'])
def send_welcome(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	cats = types.KeyboardButton('Funny Cats')
	dogs = types.KeyboardButton('Funny Dogs')
	markup.add(cats, dogs)

	#bot.reply_to(message, f"{message.chat.id}, how are you doing?")
	bot.send_message(message.chat.id, message, reply_markup=markup)

@bot.message_handler(content_types=['text'])
def send_answer(message):
	if message.text == 'Funny Cats' or message.text == 'Funny Dogs':
		track = check_time(mes_time=message.date)
		animal = message.text.split(' ')[-1]
		if track:
			images = get_local_photo(animal=animal.lower()[:-1])
			for image in images:
				bot.send_photo(message.chat.id, photo=image)
		else:
			par = Parser()
			images = par.get_images(key_word=message.text)
			for image in images:
				bot.send_photo(message.chat.id, photo=image)

	elif message.text == 'test':

		bot.send_message(message.chat.id, message.date)

@bot.message_handler(content_types=['photo'])
def test_answer(message):
	bot.reply_to(message.chat.id, "photo")

@bot.message_handler(content_types=['document'])
def test_answer(message):
	bot.reply_to(message.chat.id, "document")

bot.infinity_polling()
#1652889620
#1652889824