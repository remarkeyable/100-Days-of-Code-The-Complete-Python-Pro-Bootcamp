from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from colorthief import ColorThief
import matplotlib.pyplot as plt
from form import UploadImage

get_color = ColorThief('download.jpg')
ten_colors = get_color.get_palette(color_count=5)
# plt.imshow([[ten_colors[i] for i in range(9)]])


for i in ten_colors:
    print(f"RGB: {i}")
    print(f"HEX CODE: #{i[0]:02x}{i[1]:02x}{i[2]:02x}")

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def home():
    form = UploadImage()
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
