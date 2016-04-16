import config
rulesForFG = open("rulesForFG.txt", "rb").read() #rules for FG
rulesForOtherChats = 'Правила? Правило одно - никаких правил! Только безумие! Кстати, не хочешь оленьих зубов?'

voiceForFG = 'RaidCall: 12362665'
voiceForOtherChats = 'Прости, трехмерный, эта информация закрыта! Ты всего лишь пятичувственный, не поймешь...'

unauthorizedAccessDeny = 'Ага, сейчас, мясной мешок, только очки протру!'
searchEmpty = 'Тебе найти пустоту? Давай я уберу у тебя из организма кровь? Вот и найдешь!'

newChatParticipantMessage = open("newChatParticipant.txt", "rb").read() #дефолтное сообщение для newChatParticipant
newChatParticipantMessageForYL = open("newChatParticipantForYiffLover.txt", "rb").read()

startMessageFull = open("startMessageFull.txt", "rb").read() #сообщение для start, help, commands для чата FG
startMessageShort = open("startMessageShort.txt", "rb").read() #сообщение для start, help, commands для других чатов
moderatorsList = open("moderatorsList.txt", "rb").read()


inviteLinkForOtherChats = 'Пригласить тебя ко мне в измерение? А ты уверен, что так хочешь этого? Ну ладно! Просто иди сюда: ' + config.inviteLink

masterContacts = 'Skype создателя: ten_millionfireflies, tlgrm: @ten_million_fireflies'
getCodeBot = 'Исходный код бота: https://github.com/LokiL/WatchingEyeBot \nИспользуемый API: https://github.com/eternnoir/pyTelegramBotAPI'
exceptionText = 'Exception raised!'
dealText = 'Кто-то сказал \'сделка\'? И что же ты хочешь от меня, а, мягкотелый?'