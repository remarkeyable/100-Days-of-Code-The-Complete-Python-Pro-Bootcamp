import requests
import wget
from flask import Flask, render_template, redirect, url_for, send_from_directory
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
    submit = SubmitField('Download')


@app.route('/', methods=['GET', 'POST'])
def home():
    form = Search()

    if form.validate_on_submit():
        tiktok_link = form.search.data

        # API
        url = "https://tiktok-video-no-watermark2.p.rapidapi.com/"

        querystring = {"url": f"{tiktok_link}", "hd": "1"}

        headers = {"X-RapidAPI-Key": "a3fc281e43msh2eaa11b1b32676ep139a38jsn52e35c774548",
                   "X-RapidAPI-Host": "tiktok-video-no-watermark2.p.rapidapi.com"}

        response = requests.get(url, headers=headers, params=querystring)

        no_watermark = response.json()['data']['play']
        print(no_watermark)

        download_folder = os.path.expanduser('~') + '\Downloads'
        filename = "test.mp4"
        wget.download(no_watermark, os.path.join(download_folder, filename))
        return redirect(url_for('home'))  # return send_from_directory(download_folder, filename, as_attachment=True)

    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
