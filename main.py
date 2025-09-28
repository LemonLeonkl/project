import telebot
import os, random
import time
import schedule
import threading
from pars_news import get_news

bot = telebot.TeleBot("")
chat_id = ''
news = get_news()

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!и Я буду рассказывать тебе свеже новости об экологии! Как захочешь почитать новости пиши /get_news!')
    
@bot.message_handler(commands=['news'])
def news(message):
    news = get_news()
    bot.reply_to(message, news)

@bot.message_handler(commands=['get_news'])
def func(message):
    global chat_id
    chat_id = message.chat.id 
    bot.reply_to(message, F'Теперь я буду каждый день в 13:00 присылать тебе новости!')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

def func1():
    schedule.every().day.at("13:00").do(func2)
    while True:
        schedule.run_pending()
        time.sleep(1)

def func2():
    bot.send_message(chat_id, get_news())

per = threading.Thread(target=func1)
per.daemon = True
per.start()

bot.polling()