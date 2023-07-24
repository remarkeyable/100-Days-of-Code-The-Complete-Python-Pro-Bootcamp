from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap4
from colorthief import ColorThief
import matplotlib.pyplot as plt
from form import UploadImage
import os
import pyperclip

app = Flask(__name__)
Bootstrap4(app)
app.config['SECRET_KEY'] = '8BYkEfBA6O6WlSihBXox7C0sKR6b'
app.config['UPLOAD_FOLDER'] = 'static/uploads'

the_image = "sample_image.jpg"
color_palette = []


def get_pal():
    global color_palette
    get_color = ColorThief(f'static/uploads/{the_image}')
    ten_colors = get_color.get_palette(color_count=10)

    for i in ten_colors:
        color_palette.append(f"#{i[0]:02x}{i[1]:02x}{i[2]:02x}")


@app.route('/', methods=['GET', 'POST'])
def home():
    global color_palette
    return render_template('index.html', file_name=the_image, color_palette=color_palette)


@app.route('/upload', methods=['POST'])
def upload():
    global the_image, color_palette
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    file_extension = os.path.splitext(file.filename)[1]
    file.save(f"{app.config['UPLOAD_FOLDER']}/image{file_extension}")
    color_palette = []
    the_image = f"image{file_extension}"
    get_pal()

    return redirect(url_for('home'))


@app.route('/copy_code/<code>')
def copy_code(code):
    pyperclip.copy(code)
    return redirect(url_for('home'))


get_pal()
if __name__ == '__main__':
    app.run(debug=True)
