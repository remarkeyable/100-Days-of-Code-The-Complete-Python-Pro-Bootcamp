import os
from functools import wraps

from flask import Flask, render_template, redirect, request, url_for, abort, flash
from flask_bootstrap import Bootstrap
import stripe
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user, login_manager
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__, static_url_path='', static_folder='public')
app.config['SECRET_KEY'] = '8BYkEfBA6O6WlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///users.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()

# web
Bootstrap(app)
PRICE = 'price_1NhlPuGp3t8zciJQV88cgirp'
API = 'sk_test_51Nhk9xGp3t8zciJQAPM7ip9v4JYgGq5vwpGTeyIoKwNzFGT3rfg2ZJqOYvn4emRyAfXz59KuHIpMH9EjY25sfUjP00Wgc0HvMi'
YOUR_DOMAIN = 'http://localhost:4242'
stripe.api_key = API

# Authenticate
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


# database
class Users(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100))


# db.create_all()


@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    return render_template('checkout.html')


@app.route('/user_login', methods=['GET', 'POST'])
def user_login():
    username = request.form.get('username')
    password = request.form.get('password')

    if request.method == 'POST':
        print(username)
        print(password)
        user = Users.query.filter_by(user_name=username).first()
        if not user:
            flash(
                'Uh-oh, it seems like that email address is as non-existent as a unicorn. Time to dust off your magic and try again!')
            return redirect(url_for('login'))
        elif not check_password_hash(user.password, password):
            flash(
                'Access denied! Your password must have gone rogue like a spy who forgot the secret code. Better luck next time, Sherlock.')
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('checkout'))

    return redirect(url_for('login'))


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/sign', methods=['GET', 'POST'])
def success_registration():
    if request.method == "POST":
        user_name = request.form.get('username')
        email = request.form.get('email')
        # check if username or email already exist
        user = Users.query.filter_by(user_name=user_name).first()
        the_email = Users.query.filter_by(email=email).first()
        if not user and not the_email:
            hash_password = generate_password_hash(request.form.get('password'), method='pbkdf2:sha256', salt_length=8)
            new_user = Users(user_name=user_name, email=email, password=hash_password)
            db.session.add(new_user)
            db.session.commit()
        elif user:
            flash('Oopsie doodpsie, looks like someone else already snagged that username!')
            return redirect(url_for('signup'))
        elif the_email:
            flash('Email already in use. Please choose a different email or log in to your account.')
            return redirect(url_for('signup'))

    return redirect(url_for('login'))


@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(line_items=[{'price': PRICE, 'quantity': 1, }, ],
                                                          mode='payment', success_url=YOUR_DOMAIN + '/success.html',
                                                          cancel_url=YOUR_DOMAIN + '/cancel.html', )
    except Exception as e:
        return str(e)

    return redirect(checkout_session.url, code=303)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(port=4242, debug=True)
