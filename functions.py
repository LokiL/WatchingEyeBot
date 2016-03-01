from os import listdir, path, getcwd
from random import choice
from pygoogle import pygoogle # Использована патченная версия pygoogle! в классе pygoogle параметр self.rsz = RSZ_SMALL (!!!!)
import re


def getRandomFurryArt():
	dir = 'f:\OneDrive\Art\FurryArt'
	filename = choice(listdir(dir))
	fPath = path.join(dir, filename)
	return fPath

def getCurrentDir():
	cPath = ''
	cPath = getcwd()
	return cPath

def getParsed(incomeString, command): #функция парсинга строки
	parsed = incomeString.partition(command)
	
	return (parsed[0], parsed[1], parsed[2].strip())

def dictToList(inDict): #преобразуем словарь в список
        outList = []
        for key, value in inDict.items():
                temp = [key, value]            
                outList.append(temp)
        return outList

def cleanString(inString):
        outString = ''
        outString = re.sub('[\[\]]', '', inString)
        return outString

def listToStr(inList):
        outString = ''
        outString = '\n'.join([str(i)for i in inList]) #генератор для сложного преобразования списка в строку
        return outString


        

def getGoogleResult(searchQuery):
	results = pygoogle(searchQuery)
	results.pages = 1
	listOfResults = dictToList(results.search())
	strOfResults = listToStr(listOfResults)
	return cleanString(strOfResults) #возвращает форматированную строку с результатами поиска






	

	

if __name__ == "__main__":
	#print(getCurrentDir())
	#print(parseString('/google testestest testest ', '/google'))
	#print(parseString('/google testestest testest ', '/google')[1])
        a = getGoogleResult('porn')
        print(a)
        print(cleanString('[Gravity Falls (TV Series 2012– ) - IMDb' 'http://www.imdb.com/title/tt1865718/]'))
                
                
        
	

	#messageLast = ''

#@bot.message_handler(func=lambda m: True)
#def echo(message):
	#messageLast = str(message.text)
	#bot.reply_to(message, messageLast)

