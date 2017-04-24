# _*_coding: utf-8 _*_

"""
It's a file with main logic. It receives a users requests (user_id and movie name) and pass it to dbcontrol.py.
Later it receives ready-signal from checker.py when it found a fresh release. After Main.py gets an update for user
from DBcontol.py (user_id, movie name, link to the movie) and send it to user.

Commands like /start and /help and /rate (poll for a bot rating) also described here.
"""

import collections
import telebot
import config


bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Please send a movie name using /remind_me command. E.g. /remind_me Star Trek")


@bot.message_handler(commands=['remind_me'])
def confirm_request(message):
    bot.reply_to(message, "Thanks, you'll be notified when movie is released on DVD")

bot.polling()