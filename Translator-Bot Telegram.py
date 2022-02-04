import sqlite3
import telebot
from googletrans import Translator
from telebot import types
from peewee import *

translator=Translator()

bot=telebot.TeleBot("TOKEN")

conn=SqliteDatabase('database.db')

class BaseModel(Model):
    class Meta:
        database=conn

class USER(BaseModel):
    id=AutoField(column_name='id')
    first_name=TextField(column_name='first_name', null=True)
    surname=TextField(column_name='surname', null=True)
    username=TextField(column_name='username', null=True)
    
    class Meta:
        table_name='USER'
        
@bot.message_handler(commands=['start']) #Function for checking and creating user in database
def start_message(message):
    id=message.from_user.id
    first_name=message.from_user.first_name
    surname=message.from_user.last_name
    username=message.from_user.username           
    try: 
        USER.create(id=id, first_name=first_name, surname=surname, username=username)
        bot.send_message(message.chat.id, "Hello, I'm Mr. Cat. I have a linguistic and philological cat's education. Now I know 12 the most popular languages.\n\n For reading the instruction tap /help")
    except:
        bot.send_message(message.chat.id, "Write me a text in any language and I will translate it.")	    	      	
                       
@bot.message_handler(commands=['help']) #Function for /help
def message(message):
    bot.send_message(message.chat.id, "Instructions for use\n1. Write text in Russian, English, Arabic, Chinese (simplified), French, German, Italian, Japanese, Polish, Portuguese, Spanish or Turkish without\n2. Send text\n3. Choose a translation language\n4. Your text is ready!\n5. You can click on another language button to translate this text into it\n6. You can write and send a new text to translate it\n\nCommunication Contact:CONTACT.")	
		
lang_dict={
    'ru':'russian',
    'en':'english',
    'ar':'arabic',
    'zh-cn':'chinese (simplified)',
    'fr':'french',
    'de':'german',
    'it':'italian',
    'ja':'japanese',
    'pl':'polish',
    'pt':'portuguese',
    'es':'spanish',
    'tr':'turkish',
    }	
	
lang_btns=types.InlineKeyboardMarkup(row_width=3)
rubtn=types.InlineKeyboardButton(text='russian', callback_data='ru')
enbtn=types.InlineKeyboardButton(text= 'english', callback_data= 'en')
cnbtn=types.InlineKeyboardButton(text='chinese', callback_data='zh-cn')
frbtn=types.InlineKeyboardButton(text='french', callback_data='fr')
debtn=types.InlineKeyboardButton(text='german', callback_data='de')
itbtn=types.InlineKeyboardButton(text='italian', callback_data='it')
arbtn=types.InlineKeyboardButton(text='arabic', callback_data='ar')
jabtn=types.InlineKeyboardButton(text='japanese', callback_data='ja')
plbtn=types.InlineKeyboardButton(text='polish', callback_data='pl')
ptbtn=types.InlineKeyboardButton(text='portuguese', callback_data='pt')
esbtn=types.InlineKeyboardButton(text='spanish', callback_data='es')
trbtn=types.InlineKeyboardButton(text='turkish', callback_data='tr')

lang_btns.add(rubtn, enbtn, arbtn, cnbtn, frbtn, debtn, itbtn, jabtn, plbtn, ptbtn, esbtn, trbtn)

mes=['',0]

@bot.message_handler(func=lambda message: True) #Function for understanding the text
def messager(message): 
        mes[0]=message.text
        mes[1]=message.chat.id
        if mes[0].isdigit():
            bot.send_message(mes[1], "I don't understand you, write only text, please")
        else:	
            bot.send_message(mes[1], 'Choose language for translation', reply_markup=lang_btns)
	    	    
@bot.callback_query_handler(func=lambda call:True) #Function for translating
def callback_query(call):
	message_chat_id=mes[1]
	message_text=mes[0]
	translated_message=translator.translate(message_text, dest=call.data)
	message_send={translated_message.text}
	bot.send_message(message_chat_id, text=message_send)		
    
bot.polling(none_stop=True)
