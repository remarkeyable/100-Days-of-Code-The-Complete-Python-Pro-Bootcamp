from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap4
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
from sqlalchemy import asc
import os

##CREATE DB

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap4(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collections.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()


# FORM

class ReviewForm(FlaskForm):
    rating = StringField('Your Rating out of 10 e.g 7.5', validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Done')


class AddMovie(FlaskForm):
    add_movie = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')


##CREATE TABLE
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)


db.create_all()


@app.route("/")
def home():
    all_movies = Movie.query.order_by(asc(Movie.rating)).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
        with app.app_context():
            db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route('/update', methods=['GET', 'POST'])
def update():
    form = ReviewForm()
    if form.validate_on_submit():
        new_rate = request.form['rating']
        new_review = request.form['review']
        movie_id = request.args.get('id')
        movie_to_update = Movie.query.get(movie_id)
        movie_to_update.rating = new_rate
        movie_to_update.review = new_review
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', form=form)


@app.route('/delete', methods=['GET', 'POST'])
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/add_movie', methods=['GET', 'POST'])
def add_movie():
    form = AddMovie()
    if form.validate_on_submit():
        movie = request.form['add_movie']
        tmdb_url = "https://api.themoviedb.org/3/search/movie"
        api_key = ""
        params = {"api_key": api_key, "query": movie}
        response = requests.get(url=tmdb_url, params=params)
        movie_data = response.json()['results']
        print(movie_data)
        return render_template('select.html', form=form, movie_data=movie_data)
    return render_template('add.html', form=form)


@app.route('/new')
def new_movie():
    movie_id = request.args.get("id")
    tmdb_url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    api_key = ""
    params = {"api_key": api_key}
    response = requests.get(url=tmdb_url, params=params)
    movie_data = response.json()
    new_movie = Movie(title=movie_data['original_title'], year=movie_data['release_date'].split("-")[0],
                      description=movie_data['overview'], rating=0, ranking=10, review="_",
                      img_url=f"https://image.tmdb.org/t/p/w500{movie_data['poster_path']}")
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
