from flask import Flask, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.functions import current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from functools import wraps
from flask import abort
from forms import Loginform, Update, Add

# CONNECT TO DB
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6WlSihBXox7C0sKR6b'
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///cafes.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()

ITEMS_PER_PAGE = 6

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(int(user_id))


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


class Admin(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    # def __init__(self, email, password):  #     self.email = email  #     self.password = generate_password_hash(password)


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


@app.route('/adm_login', methods=['GET', 'POST'])
def adm_login():
    form = Loginform()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = Admin.query.filter_by(email=email).first()
        if not user:
            flash(
                'Uh-oh, it seems like that email address is as non-existent as a unicorn. Time to dust off your magic and try again!')
            return redirect(url_for('adm_login'))
        elif not check_password_hash(user.password, password):
            flash(
                'Access denied! Your password must have gone rogue like a spy who forgot the secret code. Better luck next time, Sherlock.')
            return redirect(url_for('adm_login'))
        else:
            login_user(user)
            print(current_user.id)
            return redirect(url_for('index'))
    return render_template('login.html', form=form, current_user=current_user)


@app.route('/update/<int:cafe_id>', methods=['GET', 'POST'])
@admin_only
def update(cafe_id):
    cafes = Cafe.query.all()
    cafe = Cafe.query.get(cafe_id)
    edit_form = Update()
    if edit_form.validate_on_submit():
        cafe.has_sockets = edit_form.sockets.data
        cafe.has_toilet = edit_form.toilets.data
        cafe.has_wifi = edit_form.wifi.data
        cafe.can_take_calls = edit_form.calls.data
        cafe.seats = edit_form.seats.data
        cafe.coffee_price = edit_form.price.data
        db.session.commit()
        return redirect((url_for('details', cafe_id=cafe_id)))
    return render_template('edit.html', edit_form=edit_form, cafe_id=cafe_id, cafes=cafes)


@app.route('/add', methods=['GET', 'POST'])
@admin_only
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


@app.route('/logout')
@admin_only
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/delete/<cafe_id>')
@admin_only
def delete(cafe_id):
    to_delete = Cafe.query.get(cafe_id)
    db.session.delete(to_delete)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
