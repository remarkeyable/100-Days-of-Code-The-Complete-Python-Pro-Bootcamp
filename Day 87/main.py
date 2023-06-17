from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from typing_extensions import dataclass_transform
from sqlalchemy import asc

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

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


db.create_all()


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


if __name__ == '__main__':
    app.run(debug=True)
