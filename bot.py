# -*- coding: utf-8 -*-
import telebot
import config
import botToken #contains token = '<token_here>'
import localization
from functions import getRandomFurryArt

bot = telebot.TeleBot(botToken.token)

@bot.message_handler(commands=['help', 'commands', 'start'])
def send_message(message):
	if message.chat.id == config.furryGamersChatId: #Блок для чата Furry Gamers
		try:
			msg = bot.send_message(message.chat.id, localization.startMessageFull)
		except Exception:
			msg = bot.send_message(message.chat.id, localization.exceptionText)
	else:
		try:
			msg = bot.send_message(message.chat.id, localization.startMessageShort)
		except Exception:
			msg = bot.send_message(message.chat.id, localization.exceptionText)

@bot.message_handler(commands=['rules'])
def send_message(message):
	if message.chat.id == config.furryGamersChatId: #Блок для чата Furry Gamers
		try:
			msg = bot.send_message(message.chat.id, localization.rulesForFG)
		except Exception:
			msg = bot.send_message(message.chat.id, localization.exceptionText)
	else:
		try:
			msg = bot.send_message(message.chat.id, localization.rulesForOtherChats)
		except Exception:
			msg = bot.send_message(message.chat.id, localization.exceptionText)
		

@bot.message_handler(commands=['voice', 'raidcall'])
def send_message(message):
	if message.chat.id == config.furryGamersChatId: #Блок для чата Furry Gamers
		try:
			msg = bot.send_message(message.chat.id, localization.voiceForFG)
		except Exception:
			msg = bot.send_message(message.chat.id, localization.exceptionText)
	else:
		try:
			msg = bot.send_message(message.chat.id, localization.voiceForOtherChats)
		except Exception:
			msg = bot.send_message(message.chat.id, localization.exceptionText)

@bot.message_handler(commands=['contact'])
def send_message(message):
	try:
		msg = bot.send_message(message.chat.id, localization.contactSkype)
	except Exception:
		msg = bot.send_message(message.chat.id, localization.exceptionText)

@bot.message_handler(content_types=['new_chat_participant'])
def send_message(message):
	if message.chat.id == config.furryGamersChatId: #Блок для чата Furry Gamers
		try:
			msg = bot.send_message(message.chat.id, localization.newChatParticipantMessage)
		except Exception:
			msg = bot.send_message(message.chat.id, localization.exceptionText)
	else:
		pass
	
@bot.message_handler(commands=['getcode'])
def send_message(message):
	try:
		msg = bot.send_message(message.chat.id, localization.getCodeBot)
	except Exception:
		msg = bot.send_message(message.chat.id, localization.exceptionText)

@bot.message_handler(commands=['invitelink'])
def send_message(message):
	if message.chat.id == config.furryGamersChatId: #Блок для чата Furry Gamers
		try:
			msg = bot.send_message(message.chat.id, config.inviteLink)
		except Exception:
			msg = bot.send_message(message.chat.id, localization.exceptionText)
	else:
		try:
			msg = bot.send_message(message.chat.id, localization.inviteLinkForOtherChats)
		except Exception:
			msg = bot.send_message(message.chat.id, localization.exceptionText)
			
@bot.message_handler(commands=['furryart'])
def send_message(message):
	try:
		photo = open(str(getRandomFurryArt()), 'rb')
		bot.send_photo(message.chat.id, photo)
	except Exception:
		msg = bot.send_message(message.chat.id, localization.exceptionText)

@bot.message_handler(commands=['getchatid'])
def send_message(message):
	try:
		msg = bot.send_message(message.chat.id, str(message.chat.id))
	except Exception:
		msg = bot.send_message(message.chat.id, localization.exceptionText)

	

bot.polling()

while True:
	pass