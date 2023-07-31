from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

# Initialize Flask app
app = Flask(__name__)

# Set Flask app configuration settings
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie-collection.db"

# Initialize sqlalchemy object for database access
db = SQLAlchemy()
db.init_app(app)

# Movie model definition
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    year = db.Column(db.String)
    description = db.Column(db.String)
    rating = db.Column(db.String)
    ranking = db.Column(db.String)
    review = db.Column(db.String)
    img_url = db.Column(db.String)

    def __repr__(self):
        return f'<Book {self.title}>'

# Form definition for rating movies
class RateMovieForm(FlaskForm):
    rating = StringField('Your Rating Out of 10', validators=[DataRequired()])
    review = StringField('Your movie review', validators=[DataRequired()])
    submit = SubmitField('Done')

# Form definition to search for movie to add
class AddMovieForm(FlaskForm):
    movie_title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Search')

# Create database tables
with app.app_context():
    db.create_all()

# Index/home page view function to display list of all movies
@app.route("/")
def home():
    # Retrieve all movies from the database and order by name
    all_movies = db.session.execute(db.select(Movie).order_by(Movie.title)).scalars().all()

    # Update ranking of movies by reversing their order
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()

    # Render homepage with list of movies
    return render_template('index.html', all_movies=all_movies)

# Edit rating page view function
@app.route('/edit/<int:movie_id>', methods=['GET', 'POST'])
def edit_rating(movie_id):
    # Retrieve movie to edit from the database
    movie_to_update = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()

    # Handle form submission to update movie rating and review in database
    form = RateMovieForm()
    if form.validate_on_submit():
        if request.method == 'POST':
            ranking, new_review = form.rating.data, form.review.data
            movie_to_update.ranking = ranking
            movie_to_update.review = new_review
            db.session.add(movie_to_update)
            db.session.commit()
            return redirect(url_for('home'))

    # Render page with form to edit movie rating and review
    return render_template('edit.html', form=form, movie_name=movie_to_update.title)

# Delete movie view function
@app.route('/delete/<int:movie_id>', methods=['GET', 'POST'])
def delete_movie(movie_id):
    movie_to_delete = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

# Add movie view function
@app.route('/add', methods=['GET', 'POST'])
def add_movie():
    # Handle form submission to search for movie to add
    form = AddMovieForm()
    movie_name = form.movie_title.data
    if form.validate_on_submit():
        return redirect(url_for('select', movie=movie_name))
    return render_template('add.html', form=form)

# Select movie to add view function
@app.route('/select/<string:movie>', methods=['GET', 'POST'])
def select(movie):
    # Search for movie from TMDB API
    params = {
        'query': movie,
        'api_key': '2204c57aa838a27f0f5af5ef22382e9c'
    }
    movie_details = requests.get("https://api.themoviedb.org/3/search/movie", params=params).json()['results']

    # Render page to select the movie to add
    return render_template('select.html', movie_details=movie_details)

# Add movie to database after selecting from API
@app.route('/select/<int:id>', methods=['GET', 'POST'])
def add_movie_from_select(id):
    # Retrieve movie details by ID from TMDB API
    params = {
        'api_key': '2204c57aa838a27f0f5af5ef22382e9c'
    }
    movie_details = requests.get(f"https://api.themoviedb.org/3/movie/{id}", params=params).json()

    # Create Movie object and add to database
    movie = Movie(
        title=movie_details['title'],
        year=movie_details['release_date'],
        description=movie_details['overview'],
        rating=movie_details['vote_average'],
        ranking='None',
        review='None',
        img_url="https://image.tmdb.org/t/p/w500" +
        str(movie_details['poster_path'])
    )
    db.session.add(movie)
    db.session.commit()

    # Redirect to edit page for newly added movie
    updated_movie = db.session.execute(db.select(Movie).where(Movie.title == movie_details['title'])).scalar()
    return redirect(url_for('edit_rating', movie_id=updated_movie.id))

# Main function to run Flask app
if __name__ == '__main__':
    app.run(debug=True)