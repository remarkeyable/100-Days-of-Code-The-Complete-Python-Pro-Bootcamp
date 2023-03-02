import requests
from bs4 import BeautifulSoup
import spotipy
import os
import telebot
import datetime
from spotipy.oauth2 import SpotifyOAuth
GREETINGS = "Greetings, hooman! Are you ready to groove to some seriously throwback tunes? " \
            "'Cause I'm about to take you on a time-traveling musical journey! So, like, tell me, " \
            "where do you wanna go? Give me the date in this funky fresh format: YYYY-MM-DD, " \
            "& I'll whip up a sick Spotify playlist with the top 100 Billboard hits from that day! Let's get jiggy with it!"
WAITING = "Hold your horses, my hooman friend! I'm already in the process of cooking up a hot and spicy playlist just for you!"
ERROR = "Oopsie! Something went wrong in the tech world. Check your date format, hooman! It should look like YYYY-MM-DD, eg: 2022-01-23 . Let's try again, shall we?"


KEY = os.environ['KEY']
CLIENT= os.environ['CLIENT']
SECRET= os.environ['SECRET']
bot = telebot.TeleBot(KEY)

#Bot Starting message
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, GREETINGS)


@bot.message_handler(content_types=['text'])
#Will get the text message from user
def get_text(message):
    user_input = message.text
    date_format = '%Y-%m-%d'

    try:
        #dateObject will check if user sent a proper date format
        dateObject = datetime.datetime.strptime(user_input, date_format)
        #if user sent a wrong format, telegram bot will reply using this WAITING constant
        bot.reply_to(message, WAITING)
        request = requests.get(f"https://www.billboard.com/charts/hot-100/{user_input}/")
        result = request.text
        soup = BeautifulSoup(result, "html.parser")
        #will extract data from billboard website and turn the data into a list
        extracted = soup.select(".o-chart-results-list__item h3.c-title")
        songs = [i.getText().strip() for i in extracted]

        spotify = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                scope="playlist-modify-private",
                redirect_uri="http://localhost:8888/callback",
                client_id=CLIENT,
                client_secret=SECRET,
                show_dialog=True,
                cache_path="token.txt"
            )
        )
        year = user_input.split("-")[0]

        list = []
        for j in songs:
            result = spotify.search(q=f"track:{j} year:{year} ", type="track")
            try:
                uri = result["tracks"]["items"][0]["uri"]
                list.append(uri)
            except IndexError:
                print("skipped a song")
        #will create a spotify playlist
        playlist = spotify.user_playlist_create(user="31pwibyghqh5qfpzrvffibzyl6vy", name=f"{year} Billboard 100", public=False)
        #will add songs into a spotify playlist
        spotify.playlist_add_items(playlist_id=playlist["id"], items=list)
        #finally, bot will send the user a link of a spotify playlist
        bot.reply_to(message, f" Here yah go ~ \n https://open.spotify.com/playlist/{playlist['id']}")

    except ValueError:
        bot.reply_to(message, ERROR)


bot.infinity_polling()