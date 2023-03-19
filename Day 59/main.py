from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    req = requests.get('https://api.npoint.io/906adb31c902f13769de')
    result = req.json()
    return render_template('index.html', blog=result)


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/post<num>')
def postt(num):
    req = requests.get('https://api.npoint.io/906adb31c902f13769de')
    result = req.json()
    return render_template('post.html', blog=result, number=int(num))


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)
