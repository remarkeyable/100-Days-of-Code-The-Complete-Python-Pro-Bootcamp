import time
import pytube
import requests
import wget
from pytube.exceptions import VideoUnavailable, RegexMatchError
from telegram import Update
from telegram.error import TimedOut
from telegram.ext import Application, CommandHandler, filters, MessageHandler, ContextTypes
from typing import Final
import re
import os
from pytube import YouTube

KEY: Final = os.environ['KEY']
USERNAME: Final = '@fbyt_downloader_bot'
FB_TOKEN = os.environ['FB_TOKEN']



def download_yt(link):
    file_path = os.path.abspath(os.getcwd())
    yt = YouTube(link)
    video = yt.streams.get_highest_resolution()
    video.download(file_path)
    file_name = video.default_filename
    the_file = f'{file_path}/{file_name}'
    return the_file


def download_fb(link):
    file_path = os.path.abspath(os.getcwd())
    url = "https://facebook-reel-and-video-downloader.p.rapidapi.com/app/main.php"
    querystring = {"url": link}

    headers = {"X-RapidAPI-Key": "a3fc281e43msh2eaa11b1b32676ep139a38jsn52e35c774548",
               "X-RapidAPI-Host": "facebook-reel-and-video-downloader.p.rapidapi.com"}

    response = requests.get(url, headers=headers, params=querystring)

    video = response.json()['links']['Download High Quality']

    wget.download(video, 'video.mp4')
    the_file = f'{file_path}/video.mp4'
    return the_file


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hi hooman. send your fb or youtube video link, but just so you know, I'm still a bot in the making & can only "
        "handle videos up to 1 to 2 minutes long. Let's keep it short and snappy!")


async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    link = update.message.text
    file = None
    try:
        file = download_yt(link)
        await update.message.reply_text(
            "Your video is currently in the process of downloading. Please hang tight and enjoy a cup of virtual coffee while the magic happens!")
        time.sleep(5)
        await update.message.reply_video(video=open(file, 'rb'))
        os.remove(file)

    except VideoUnavailable or RegexMatchError:
        file = download_fb(link)
        await update.message.reply_text(
            "Your video is currently in the process of downloading. Please hang tight and enjoy a cup of virtual coffee while the magic happens!")
        time.sleep(5)
        await update.message.reply_video(video=open(file, 'rb'))
        os.remove(file)
    except TimedOut:
        await update.message.reply_text(
            "Error occurred, I'm still a bot in the making & can only handle videos up to 1 to 2 minutes long")
    finally:
        try:
            print('finally')
            print(file)
            os.remove(file)
        except:
            pass


if __name__ == '__main__':
    app = Application.builder().token(KEY).read_timeout(60).write_timeout(60).build()
    app.add_handler(CommandHandler('start', start))
    # message
    app.add_handler(MessageHandler(filters.TEXT, message))
    app.run_polling(poll_interval=3)
