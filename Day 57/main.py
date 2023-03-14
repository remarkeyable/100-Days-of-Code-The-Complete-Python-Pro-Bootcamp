from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    blog_post = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
    blog_main = blog_post.json()
    return render_template('index.html', blogg=blog_main)


@app.route('/blog/<num>')
def the_blog(num):
    blog_post = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
    blog = blog_post.json()
    print(num)
    print(type(num))

    return render_template('post.html', blog=blog, number=int(num))


if __name__ == '__main__':
    app.run(debug=True)
