import wget
from flask import Flask, render_template, request, send_file, redirect, url_for, after_this_request
from flask_bootstrap import Bootstrap
import requests
import os
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6WlSihBXox7C0sKR6b'
app.config['UPLOAD_FOLDER'] = 'logs'
Bootstrap(app)

ERROR = "success"


@app.route('/', methods=['GET', 'POST'])
def home():
    global ERROR
    file_name = None
    if request.method == "POST":
        tiktok_link = request.form.get('link')
        # try:
        # API
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
        # file_name = response.json()['data']['id']
        file_name = 'helooo'
        wget.download(tiktok_link, "video.png")
        ERROR = False

        @after_this_request
        def delete_file(response):
            try:
                os.remove('video.png')
            except Exception as e:
                app.logger.error("Error deleting file: %s", e)
            return response

        # send_file("video.mp4", as_attachment=True, download_name=f'{file_name}.mp4')
        return send_file("video.png", as_attachment=True,
                         download_name=f'{file_name}.mp4')  # except:  #     ERROR = True
    return render_template('index.html', error=ERROR, the_file=file_name)

#
# @app.after_request
# def after_request_func(response):
#     print("after_request executing!")
#     time.sleep(4)
#     if os.path.exists("video.mp4"):
#         os.remove("video.mp4")
#     else:
#         print("The file does not exist")
#     return response


if __name__ == '__main__':
    app.run(debug=True)
