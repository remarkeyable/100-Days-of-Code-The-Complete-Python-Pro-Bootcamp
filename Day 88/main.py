import sqlite3
from flask import Flask, render_template, redirect, url_for, flash, request,  jsonify
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user, login_manager
from functools import wraps
from flask import abort
from forms import RegisterForm, LoginForm, Task
from wtforms import BooleanField

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6WlSihBXox7C0sKR6b'
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///task.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()

# Authenticate
login_manager = LoginManager()
login_manager.init_app(app)




@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


class Users(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100))


class TheTasks(db.Model):
    __tablename__ = "thetasks"
    id = db.Column(db.Integer, primary_key=True)
    # user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    done = db.Column(db.Boolean, default=False)
    task = db.Column(db.String(500), nullable=False)


# db.create_all()
# def create_user():
#     email = "sample@gmail.com"
#     password = "testing1234"
#     user = Users(email=email, password=password)
#     db.session.add(user)
#     db.session.commit()

list_of_task = []


class ModifiedTask(TheTasks):
    text = BooleanField('New Label')


@app.route('/', methods=['GET', 'POST'])
def index():
    global list_of_task
    form = Task()
    task = TheTasks.query.all()
    print(task)

    if form.validate_on_submit():
        new_task = TheTasks(task=form.task.data)
        db.session.add(new_task)
        db.session.commit()

        list_of_task.append(form.task.data)
        return redirect(url_for('index'))
    return render_template('index.html', form=form, task=task)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.submit.data:
            hash_password = generate_password_hash(form.password.data, method='pbkdf2:sha256', salt_length=8)
            new_user = Users(email=form.email.data, password=hash_password, user_name=form.username.data)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('index'))

    elif form.signin.data:
        return redirect(url_for('signin'))
    return render_template('signup.html', form=form)


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        if form.submit.data:
            user = Users.query.filter_by(email=email).first()
            if not user:
                flash(
                    'Uh-oh, it seems like that email address is as non-existent as a unicorn. Time to dust off your magic and try again!')
                return redirect(url_for('signin'))
            elif not check_password_hash(user.password, password):
                flash(
                    'Access denied! Your password must have gone rogue like a spy who forgot the secret code. Better luck next time, Sherlock.')
                return redirect(url_for('signin'))
            else:
                login_user(user)
                return redirect(url_for('index'))

    elif form.signup.data:
        return redirect(url_for('signup'))

    return render_template('signin.html', form=form)

@app.route('/done/<int:task_id>')
def done(task_id):
    edit_task = TheTasks.query.get(int(task_id))
    edit_task.done = True
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/undone/<int:task_id>')
def undone(task_id):
    edit_task = TheTasks.query.get(int(task_id))
    edit_task.done = False
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/delete/<int:task_id>')
def delete(task_id):
    delete_task = TheTasks.query.get(int(task_id))
    db.session.delete(delete_task)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
