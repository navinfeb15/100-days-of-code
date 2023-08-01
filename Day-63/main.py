from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

# Create a SQLAlchemy instance
db = SQLAlchemy()

# Initialize the Flask app
app = Flask(__name__)

# Configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"

# Initialize the app with the SQLAlchemy extension
db.init_app(app)

# Define the Book model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    author = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    
    def __repr__(self):
        return f'<Book {self.title}>'
    
# Create the database tables
with app.app_context():
    db.create_all()

# Route for the homepage
@app.route('/')
def home():
    # Retrieve all books from the database and order them by title
    all_books = db.session.execute(db.select(Book).order_by(Book.title)).scalars()
    return render_template('index.html', books=all_books)

# Route for adding a new book
@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        # Create a new Book instance with data from the form
        added_book = Book()
        added_book.title = request.form["book_name"]
        added_book.author = request.form["book_author"]
        added_book.rating = request.form["book_rating"]
        
        # Add the new book to the session and commit the changes
        db.session.add(added_book)
        db.session.commit()
        
        return redirect(url_for('home'))
    
    return render_template('add.html')

# Route for editing a book's rating
@app.route('/edit/<int:book_id>', methods=['GET', 'POST'])
def change_rating(book_id):
    # Retrieve the book details based on the provided book_id
    book_details = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    
    if request.method == 'POST':
        # Update the book's rating with the new value from the form
        new_rating = request.form["new_rating"]
        book_details.rating = new_rating
        db.session.commit()
        
        return redirect(url_for('home'))
    
    return render_template('book.html', book=book_details)

# Route for deleting a book
@app.route('/delete/<int:book_id>', methods=['GET', 'POST'])
def delete_book(book_id):
    # Retrieve the book to delete based on the provided book_id
    book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    
    # Delete the book and commit the changes
    db.session.delete(book_to_delete)
    db.session.commit()
    
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
