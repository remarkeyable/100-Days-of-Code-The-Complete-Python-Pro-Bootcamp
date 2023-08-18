import requests
import wget
from flask import Flask, render_template, redirect, url_for, send_from_directory, request
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6WlSihBXox7C0sKR6b'
Bootstrap5(app)

ERROR = "success"


# Forms
class Search(FlaskForm):
    search = StringField('Tiktok Video Link', validators=[DataRequired()])
    submit = SubmitField('Download')


@app.route('/', methods=['GET', 'POST'])
def home():
    global ERROR



    if request.method == "POST":
        try:
            # tiktok_link = request.form.get('link')
            #
            # # API
            # url = "https://tiktok-video-no-watermark2.p.rapidapi.com/"
            #
            # querystring = {"url": f"{tiktok_link}", "hd": "1"}
            #
            # headers = {"X-RapidAPI-Key": "a3fc281e43msh2eaa11b1b32676ep139a38jsn52e35c774548",
            #            "X-RapidAPI-Host": "tiktok-video-no-watermark2.p.rapidapi.com"}
            #
            # response = requests.get(url, headers=headers, params=querystring)
            #
            # no_watermark = response.json()['data']['play']
            # print(no_watermark)
            #
            # download_folder = os.path.expanduser('~') + '\Downloads'
            # filename = "tiktok.mp4"
            # wget.download(no_watermark, os.path.join(download_folder, filename))
            ERROR = True
            return redirect(url_for('home'))
        except:
            ERROR = True

    return render_template('index.html', error=ERROR)


if __name__ == '__main__':
    app.run(debug=True)
