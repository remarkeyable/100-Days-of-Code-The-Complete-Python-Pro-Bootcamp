import os, shutil, tempfile
import tempfile
import wget
from flask import Flask, render_template, request, send_file
from flask_bootstrap import Bootstrap
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6WlSihBXox7C0sKR6b'
app.config['UPLOAD_FOLDER'] = 'logs'
Bootstrap(app)

ERROR = "success"
DELETE = False


@app.route('/', methods=['GET', 'POST'])
def home():
    global ERROR, DELETE
    file_name = None
    if request.method == "POST":
        tiktok_link = request.form.get('link')
        try:
            # API
            url = "https://tiktok-video-no-watermark2.p.rapidapi.com/"

            querystring = {"url": f"{tiktok_link}", "hd": "1"}

            headers = {"X-RapidAPI-Key": "a3fc281e43msh2eaa11b1b32676ep139a38jsn52e35c774548",
                       "X-RapidAPI-Host": "tiktok-video-no-watermark2.p.rapidapi.com"}

            response = requests.get(url, headers=headers, params=querystring)

            no_watermark = response.json()['data']['play']
            file_name = response.json()['data']['id']

            wget.download(no_watermark, "static/video.png")
            path = os.path.join(app.static_folder, 'video.png')
            #delete the file after down
            cache = tempfile.NamedTemporaryFile()
            with open(path, 'rb') as fp:
                shutil.copyfileobj(fp, cache)
                cache.flush()
            cache.seek(0)
            os.remove(path)
            ERROR = False
            return send_file(cache, as_attachment=True, download_name=f"{file_name}.mp4")
        except:
            ERROR = True

    return render_template('index.html', error=ERROR, the_file=file_name)


if __name__ == '__main__':
    app.run(debug=True)
