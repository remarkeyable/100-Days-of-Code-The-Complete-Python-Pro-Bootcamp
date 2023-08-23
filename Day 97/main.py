import os
from flask import Flask, render_template, redirect, request, url_for
from flask_bootstrap import Bootstrap
import stripe
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user, login_manager
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

app = Flask(__name__, static_url_path='', static_folder='public')
app.config['SECRET_KEY'] = '8BYkEfBA6O6WlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///users.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()

# web
Bootstrap(app)
API = os.environ['KEY']
PRICE = os.environ['PRICE']
YOUR_DOMAIN = 'http://localhost:4242'
stripe.api_key = API


# database

class Users(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100))


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('checkout.html')


@app.route('/login', methods=['GET', 'POST'])
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
        hash_password = generate_password_hash(request.form.get('password'), method='pbkdf2:sha256', salt_length=8))
        new_user = Users(user_name=user_name, email=email, password=hash_password)
        db.session.add(new_user)

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


if __name__ == '__main__':
    app.run(port=4242, debug=True)
