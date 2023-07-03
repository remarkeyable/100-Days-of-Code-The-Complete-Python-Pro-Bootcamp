from flask import Flask, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user, login_manager
from functools import wraps
from flask import abort
from forms import RegisterForm, LoginForm

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
def load_use(user_id):
    return Users.query.get(int(user_id))


class Users(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100))


class TheTasks(db.Model):
    __tablename__ = "thetasks"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    task = db.Column(db.String(500), nullable=False)


# def create_user():
#     email = "sample@gmail.com"
#     password = "testing1234"
#     user = Users(email=email, password=password)
#     db.session.add(user)
#     db.session.commit()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup')
def signup():
    form = RegisterForm()


    return render_template('signup.html', form=form)


@app.route('/signin')
def signin():
    form = LoginForm()
    return render_template('signup.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
