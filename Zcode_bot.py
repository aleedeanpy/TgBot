import telebot
from telebot import types
import time 
import venv

api_token='8165528797:AAFGwWgUdEYjdUWumSNl1PAOBvJ0xSNj740'

bot=telebot.TeleBot(api_token)

@bot.message_handler(commands=['start','img'])
def handle_start(message):
    keybrd=types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1=types.KeyboardButton('Zcode')
    button2=types.KeyboardButton('Zmath')
    button3=types.KeyboardButton('Обу ҳаво-онлайн ⛈')
    button4=types.KeyboardButton('Help')
    # ln=types.KeyboardButtonRequestChat('Help',url='https://t.me/PmCodeM')
    
    # print(nam)
    keybrd.add(button1,button2,button3,button4)
    # keybrd.add(ln)

    bot.send_photo(message.chat.id,open('img1.JPG','rb'),caption="""Здравствуйте! Я ZcodeBot👨‍🔧 \nДля скачивания наших программ читайте ниже:

/zcode- Zcode
/zmath- Zmath
                 
Бот для прогноза погоды:
@ZCoderBot - Обу ҳаво-онлайн

Наш Телеграм канал:                 
Zcode ТГ канал: t.me/PmCodeM
                 
                 
                 """,reply_markup=keybrd)
    
@bot.message_handler(content_types=['text'])
def handle_message(message):
    if message.text=='Zcode' or message.text=='/zcode':
        bot.send_photo(message.chat.id,open('img.JPG','rb'),caption="""
                       
About Programm💻: Zcode
                                          
Program📀: Zcode Setup
Version: 1.0.7
Format: .exe
Programming language:Python 
                                          
Developer👨‍🔧: @mrmzcode
Assistant👨‍💻: @aleedeanpy

Link for download:
http://mrmzcode.itch.io/zcode
                       
                       """)
      


#         bot.reply_to(message,"""
        
# About Programm💻: Zcode
                                          
# Program📀: Zcode Setup
# Version: 1.0.7
# Format: .exe
# Programming language:Python 
                                          
# Developer👨‍🔧: @mrmzcode
# Assistant👨‍💻: @aleedeanpy

# Link for download:
# http://mrmzcode.itch.io/zcode""")

    if message.text=='Zmath' or message.text=='/zmath':
        time.sleep()
        bot.send_photo(message.chat.id,open('img1.JPG','rb'),caption="""
                       
About Programm💻: Zmath
                                          
Program📀: Zmath Setup
Version: 1.0.7
Format: .exe
Programming language:Python 
                                          
Developer👨‍🔧: @mrmzcode
Assistant👨‍💻: @aleedeanpy

Link for download:
http://mrmzcode.itch.io/zmath
                       
                       """)
#         bot.reply_to(message,"""
       
# About Programm💻: Zmath
                                          
# Program📀: Zmath Setup
# Version: 1.0.7
# Format: .exe
# Programming language:Python 
                                          
# Developer👨‍🔧: @mrmzcode
# Assistant👨‍💻: @aleedeanpy

# Link for download:
# http://mrmzcode.itch.io/zmath
#                      """)


    if message.text=='Обу ҳаво-онлайн ⛈':
        bot.reply_to(message,"""

Бот для прогноз погоды:                     
@ZcoderBot
                     """)
        
    if message.text=='Help':
        bot.reply_to(message,"""
Если вы что-то не понимаете или не можете работать с ботом пишите сюда:                     
Ассистент: @aleedeanpy
                     """)
        
    if message.text=='code':
        bot.reply_to(message.chat.id,"```print('hello world')```")
bot.infinity_polling(none_stop=True)