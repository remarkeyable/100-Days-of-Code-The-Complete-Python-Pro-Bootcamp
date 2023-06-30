from flask import Flask, render_template
from forms import Task

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6WlSihBXox7C0sKR6b'


@app.route('/')
def index():
    add_task = Task()
    return render_template('index.html', add_task=add_task)



if __name__ == '__main__':
    app.run(debug=True)