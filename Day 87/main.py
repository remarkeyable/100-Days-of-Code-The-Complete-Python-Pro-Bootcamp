from flask import Flask, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import current_user
from werkzeug.security import generate_password_hash
from functools import wraps
from flask import abort
from wtforms.validators import DataRequired, URL, Email

from forms import Loginform, Update, Add

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6WlSihBXox7C0sKR6b'
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///cafes.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()

items = ['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5', 'Item 6', 'Item 7', 'Item 8', 'Item 9', 'Item 10']
ITEMS_PER_PAGE = 6


class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    map_url = db.Column(db.String)
    img_url = db.Column(db.String)
    location = db.Column(db.String)
    has_sockets = db.Column(db.Boolean)
    has_toilet = db.Column(db.Boolean)
    has_wifi = db.Column(db.Boolean)
    can_take_calls = db.Column(db.Boolean)
    seats = db.Column(db.Integer)
    coffee_price = db.Column(db.Float)


# class Admin(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(128), nullable=False)
#
#     def __init__(self, email, password):
#         self.email = email
#         self.password = generate_password_hash(password)

db.create_all()


# @app.route('/create_admin')
# def create_admin():
#     admin_email = 'sample_admin@gmail.com'
#     admin_password = 'testing1234'
#     admin = Admin(email=admin_email, password=admin_password)
#     db.session.add(admin)
#     db.session.commit()
#     return f'Admin user created with email: {admin_email}'


def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            user_id = current_user.id
        except:
            user_id = 0
        if user_id == 1:
            return f(*args, **kwargs)
        else:
            return abort(403)

    return decorated_function


@app.route('/')
def index():
    cafes = Cafe.query.all()
    page = int(request.args.get('page', 1))
    total_pages = (len(cafes) + ITEMS_PER_PAGE - 1) // ITEMS_PER_PAGE
    start_index = (page - 1) * ITEMS_PER_PAGE
    end_index = start_index + ITEMS_PER_PAGE
    current_items = cafes[start_index:end_index]
    return render_template('index.html', items=current_items, page_nums=range(1, total_pages + 1), current_page=page,
                           has_prev=(page > 1), has_next=(page < total_pages), prev_page=(page - 1),
                           next_page=(page + 1))


@app.route('/details/<int:cafe_id>')
def details(cafe_id):
    cafes = Cafe.query.all()
    cafe_id = cafe_id
    return render_template('details.html', cafe=cafes, id=cafe_id)


@app.route('/adm_login')
def adm_login():
    form = Loginform()
    return render_template('login.html', form=form)


@app.route('/update/<int:cafe_id>', methods=['GET', 'POST'])
def update(cafe_id):
    cafe = Cafe.query.get(cafe_id)
    edit_form = Update()
    if edit_form.validate_on_submit():
        print(edit_form.sockets.data)
        cafe.has_sockets = edit_form.sockets.data
        cafe.has_toilet = edit_form.toilets.data
        cafe.has_wifi = edit_form.wifi.data
        cafe.can_take_calls = edit_form.calls.data
        cafe.seats = edit_form.seats.data
        cafe.coffee_price = edit_form.price.data
        db.session.commit()
        return redirect((url_for('details', cafe_id=cafe_id)))
    return render_template('edit.html', edit_form=edit_form)


@app.route('/add', methods=['GET', 'POST'])
def add():
    add_cafe = Add()
    if add_cafe.validate_on_submit():
        new_cafe = Cafe(name=add_cafe.name.data, map_url=add_cafe.map.data, img_url=add_cafe.img.data,
                        location=add_cafe.location.data, has_sockets=bool(add_cafe.sockets.data),
                        has_toilet=bool(add_cafe.toilets.data), has_wifi=bool(add_cafe.wifi.data),
                        can_take_calls=bool(add_cafe.calls.data), seats=add_cafe.seats.data,
                        coffee_price=add_cafe.price.data)
        db.session.add(new_cafe)
        db.session.commit()
        return redirect((url_for('index')))
    return render_template('add.html', add_cafe=add_cafe)


if __name__ == '__main__':
    app.run(debug=True)
