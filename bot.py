# -*- coding: utf-8 -*-
import os
import logging
import telegram
from telegram.error import NetworkError, Unauthorized
from telegram.ext import Updater
from time import sleep
from telegram.ext import CommandHandler
import os
import random

REQUEST_KWARGS = {
    "proxy_url": ""
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
        if son_dir[i][-4:] == '.jpg' or\
                son_dir[i][-4:] == '.png' or\
                son_dir[i][-5:] == '.jpeg' or\
                son_dir[i][-5:] == '.webp' or\
                son_dir[i][-4:] == '.JPG' or\
                son_dir[i][-4:] == '.gif':
            link.append(randp + '/' + son_dir[i])
    link_rand = random.randint(0, len(link)-1)
    context.bot.send_photo(chat_id=update.effective_chat.id,photo=open("./Dress/" + link[link_rand] , 'rb'))

launcher_handler = CommandHandler("launch", launch)

dress_handler = CommandHandler("dress", dress)

dispatcher.add_handler(launcher_handler)

dispatcher.add_handler(dress_handler)

updater.start_polling()
