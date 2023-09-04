import asyncio
import os
import time

from pytube import YouTube
import telebot
from telebot import types


# def download_video_from_youtube(link, path):
#     yt = YouTube(link)
#     video = yt.streams.get_highest_resolution()
#
#     # download the video
#     video.download(path)
#
# # example usage:
# download_video_from_youtube('https://www.youtube.com/watch?v=5a3IHwaZLMo', r'C:\Users\rsdelmonte_asticom\Day 99')


def download_yt(link):
    file_path = os.path.abspath(os.getcwd())
    yt = YouTube(link)
    video = yt.streams.get_highest_resolution()
    video.download(file_path)
    file_name = video.default_filename
    return file_name


download_yt("https://www.youtube.com/watch?v=0XJJCvpe7as")
#
WELCOME = 'Hi'

bot = telebot.TeleBot('6233247353:AAFL2hzx60axoCEUnPbGEEviR_Bf-v6x46U')


@bot.message_handler(commands=['start'])
def welcome_message(message):
    mark_up = types.InlineKeyboardMarkup(row_width=2)
    fb = types.InlineKeyboardButton('Facebook', callback_data='facebook')
    yt = types.InlineKeyboardButton('Youtube', callback_data='youtube')
    mark_up.add(fb, yt)
    bot.send_message(message.chat.id, 'Choose video source', reply_markup=mark_up)


@bot.callback_query_handler(func=lambda call: True)
def response(callback, context):
    if callback.message:
        if callback.data == 'facebook':
            bot.send_message(callback.message.chat.id, 'Aight! Please send the link of your facebook video.')

            @bot.message_handler()
            def get_link(message):
                chat_id = message.chat.id
                path = os.path.abspath(os.getcwd())
                fb_link = message.text
                bot.reply_to(message, "processing")
                download_yt(fb_link)
                # with open(f"{path}/{file_name}") as video_file:
                #     bot.send_video(chat_id, video_file)

        # if callback.data == 'youtube':
        #     bot.send_message(callback.message.chat.id, 'Aight! Please send the link of your youtube video.')
        #
        #     @bot.message_handler()
        #     def get_link_yt(message):
        #         bot.reply_to(message, "processing yt")


bot.infinity_polling()
