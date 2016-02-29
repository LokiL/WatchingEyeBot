from os import listdir, path
from random import choice

def getRandomFurryArt():
	dir = 'f:\OneDrive\Art\FurryArt'
	filename = choice(listdir(dir))
	fPath = path.join(dir, filename)
	return fPath

	#messageLast = ''

#@bot.message_handler(func=lambda m: True)
#def echo(message):
	#messageLast = str(message.text)
	#bot.reply_to(message, messageLast)

