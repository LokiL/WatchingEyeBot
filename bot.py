# -*- coding: utf-8 -*-
import telebot
import config
from functions import getRandomFurryArt

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['help', 'commands', 'start'])
def send_message(message):
	if message.chat.id == config.furryGamersChatId: #Блок для чата Furry Gamers
		try:
			msg = bot.send_message(message.chat.id, config.command_list)
		except Exception:
			msg = bot.send_message(message.chat.id, 'Exception raised')
	else:
		try:
			msg = bot.send_message(message.chat.id, config.welcomeMessageForOtherChats)
		except Exception:
			msg = bot.send_message(message.chat.id, 'Exception raised')

@bot.message_handler(commands=['rules'])
def send_message(message):
	if message.chat.id == config.furryGamersChatId: #Блок для чата Furry Gamers
		try:
			msg = bot.send_message(message.chat.id, config.rules)
		except Exception:
			msg = bot.send_message(message.chat.id, 'Exception raised')
	else:
		try:
			msg = bot.send_message(message.chat.id, 'Правила? Правило одно - никаких правил! Только безумие!')
		except Exception:
			msg = bot.send_message(message.chat.id, 'Exception raised')
		

@bot.message_handler(commands=['voice', 'raidcall'])
def send_message(message):
	if message.chat.id == config.furryGamersChatId: #Блок для чата Furry Gamers
		try:
			msg = bot.send_message(message.chat.id, 'RaidCall: 12362665')
		except Exception:
			msg = bot.send_message(message.chat.id, 'Exception raised')
	else:
		try:
			msg = bot.send_message(message.chat.id, 'Прости, трехмерный, эта информация закрыта! Кстати, оленьи зубы не нужны?')
		except Exception:
			msg = bot.send_message(message.chat.id, 'Exception raised')

@bot.message_handler(commands=['contact'])
def send_message(message):
	try:
		msg = bot.send_message(message.chat.id, 'Skype создателя: ten_millionfireflies')
	except Exception:
		msg = bot.send_message(message.chat.id, 'Exception raised')

@bot.message_handler(content_types=['new_chat_participant'])
def send_message(message):
	if message.chat.id == config.furryGamersChatId: #Блок для чата Furry Gamers
		try:
			msg = bot.send_message(message.chat.id, config.welcome_message)
		except Exception:
			msg = bot.send_message(message.chat.id, 'Exception raised')
	else:
		pass
	
@bot.message_handler(commands=['getcode'])
def send_message(message):
	try:
		msg = bot.send_message(message.chat.id, 'https://github.com/eternnoir/pyTelegramBotAPI')
	except Exception:
		msg = bot.send_message(message.chat.id, 'Exception raised')

@bot.message_handler(commands=['invitelink'])
def send_message(message):
	if message.chat.id == config.furryGamersChatId: #Блок для чата Furry Gamers
		try:
			msg = bot.send_message(message.chat.id, config.invitelink)
		except Exception:
			msg = bot.send_message(message.chat.id, 'Exception raised')
	else:
		try:
			msg = bot.send_message(message.chat.id, 'Пригласить тебя ко мне в измерение? А ты уверен, что так хочешь этого?')
		except Exception:
			msg = bot.send_message(message.chat.id, 'Exception raised')
		
	
@bot.message_handler(commands=['furryart'])
def send_message(message):
	try:
		photo = open(str(getRandomFurryArt()), 'rb')
		bot.send_photo(message.chat.id, photo)
	except Exception:
		msg = bot.send_message(message.chat.id, 'Exception raised')

@bot.message_handler(commands=['getchatid'])
def send_message(message):
	try:
		msg = bot.send_message(message.chat.id, str(message.chat.id))
	except Exception:
		msg = bot.send_message(message.chat.id, 'Exception raised')

	

bot.polling()

while True:
	pass