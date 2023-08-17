import requests
import wget
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6WlSihBXox7C0sKR6b'
Bootstrap5(app)


# Forms
class Search(FlaskForm):
    search = StringField('Tiktok Link', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def home():
    form = Search()

    if form.validate_on_submit():
        tiktok_link = form.search.data
        file_name = wget.filename_from_url(tiktok_link)
        wget.download(tiktok_link, file_name)

        download_folder = os.path.expanduser('~') + '\Downloads'
        os.rename(file_name, download_folder)
        return redirect(url_for('home'))

    return render_template('index.html', form=form)


# url = "https://tiktok-video-no-watermark2.p.rapidapi.com/"
#
# querystring = {"url": "https://www.tiktok.com/@marianrivera/video/7265653123367161094?lang=en", "hd": "1"}
#
# headers = {"X-RapidAPI-Key": "a3fc281e43msh2eaa11b1b32676ep139a38jsn52e35c774548",
#            "X-RapidAPI-Host": "tiktok-video-no-watermark2.p.rapidapi.com"}
#
# response = requests.get(url, headers=headers, params=querystring)
#
# no_watermark = response.json()['data']['play']
#
# print(no_watermark)


if __name__ == '__main__':
    app.run(debug=True)
