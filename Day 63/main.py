from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collections.db"
db.init_app(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

with app.app_context():
    db.create_all()


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    author = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'


@app.route('/')
def home():
    all_books = db.session.query(Books).all()
    print(all_books)
    return render_template("index.html", books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        book = request.form['books']
        author = request.form['author']
        ratings = request.form['ratings']
        with app.app_context():
            new_book = Books(title=book, author=author, rating=ratings)
            db.session.add(new_book)
            db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')


@app.route("/edit_rating/<num>", methods=['GET', 'POST'])
def edit_rating(num):
    number = int(num)
    all_books = db.session.query(Books).all()
    if request.method == 'POST':
        rating = request.form['edit']
        book_id = num
        book_to_update = Books.query.get(book_id)
        book_to_update.rating = rating
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', books=all_books, num=number)


@app.route('/delete/<num>')
def delete(num):
    book_id = num
    book_to_delete = Books.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
