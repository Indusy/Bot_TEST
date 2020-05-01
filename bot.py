# -*- coding: utf-8 -*-
import os
import logging
import telegram
from telegram.error import NetworkError, Unauthorized
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
from time import sleep
import os
import re
import random
from pydub import AudioSegment

REQUEST_KWARGS = {
    "proxy_url": "http://127.0.0.1:1080"
}

updater = Updater(
    token='',
    use_context=True,
    request_kwargs=REQUEST_KWARGS
)

dispatcher = updater.dispatcher

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)


def launch(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=("".join(context.args)))


def dress(update, context):
    link = []
    
    rand_num = random.randint(0, 233)

    parent_dir = os.listdir('./Dress')

    randp = parent_dir[rand_num]

    son_dir = os.listdir('./Dress/'+randp)

    for i in range(len(son_dir)):
    	status = 0
    	if son_dir[i][-4:] == '.jpg' or\
                son_dir[i][-4:] == '.png' or\
                son_dir[i][-5:] == '.jpeg' or\
                son_dir[i][-5:] == '.webp' or\
                son_dir[i][-4:] == '.JPG' or\
                son_dir[i][-4:] == '.gif':
            link.append(randp + '/' + son_dir[i])
            if "".join(context.args)=="list":
        	    context.bot.send_photo(chat_id=update.effective_chat.id,photo=open("./Dress/" + link[i],'rb'))
        	    status=1
    if status == 0:    	    
        link_rand = random.randint(0, len(link)-1)
        context.bot.send_photo(chat_id=update.effective_chat.id,photo=open("./Dress/" + link[link_rand] , 'rb'))
        status = 0

def oidua(update,context):
    dd_audio=context.bot.get_file(update.effective_message.audio).download(update.effective_message.audio.title)
    AudioSegment.from_mp3(dd_audio).reverse().export('./'+dd_audio+'_reversed.mp3')
    context.bot.send_audio(chat_id=update.effective_chat.id,audio=open('./'+dd_audio+'_reversed.mp3','rb'))
    os.remove('./'+update.effective_message.audio.title)
    os.remove('./'+dd_audio+'_reversed.mp3')

def eciov(update,context):
    dd_audio=context.bot.get_file(update.effective_message.voice).download('语音消息')
    AudioSegment.from_mp3(dd_audio).reverse().export('./'+dd_audio+'_reversed.mp3')
    context.bot.send_audio(chat_id=update.effective_chat.id,audio=open('./'+dd_audio+'_reversed.mp3','rb'))
    os.remove('./语音消息')
    os.remove('./语音消息'+'_reversed.mp3')

def wa(update,context):
    if '不会' in update.effective_message.text:
        context.bot.send_message(chat_id=update.effective_chat.id, text='那'+update.effective_user.first_name+'你能帮帮我吗')

launcher_handler = CommandHandler("launch", launch)

dress_handler = CommandHandler("dress", dress)

oidua_handler = MessageHandler(Filters.audio,oidua)

eciov_handler = MessageHandler(Filters.voice,eciov)

wa_handler = MessageHandler(Filters.text,wa)

dispatcher.add_handler(launcher_handler)

dispatcher.add_handler(dress_handler)

dispatcher.add_handler(oidua_handler)

dispatcher.add_handler(wa_handler)

dispatcher.add_handler(eciov_handler)

updater.start_polling()
