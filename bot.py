from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

#create the chatbot
bot = ChatBot('Test') 

#open and read conversation file
conv = open('chats.txt','r').readlines()

#set trainer
trainer = ListTrainer(bot)  
#train the bot    	    
trainer.train(conv)                 

while True:
	request = input('You: ')
	if request == 'stop':
		break
	else:
		response = bot.get_response(request)

		print('Bot: ', response) 