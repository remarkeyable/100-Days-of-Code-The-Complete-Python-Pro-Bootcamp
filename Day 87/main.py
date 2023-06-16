from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from typing_extensions import dataclass_transform

db = SQLAlchemy()
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///cafes.db"
db.init_app(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

with app.app_context():
    db.create_all()

items = ['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5', 'Item 6', 'Item 7', 'Item 8', 'Item 9', 'Item 10']

ITEMS_PER_PAGE = 6


@app.route('/')
def index():
    page = int(request.args.get('page', 1))
    total_pages = (len(items) + ITEMS_PER_PAGE - 1) // ITEMS_PER_PAGE
    start_index = (page - 1) * ITEMS_PER_PAGE
    end_index = start_index + ITEMS_PER_PAGE
    current_items = items[start_index:end_index]
    return render_template('index.html', items=current_items, page_nums=range(1, total_pages + 1), current_page=page,
                           has_prev=(page > 1), has_next=(page < total_pages), prev_page=(page - 1),
                           next_page=(page + 1))


if __name__ == '__main__':
    app.run(debug=True)
