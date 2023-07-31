from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"
# initialize the app with the extension
db.init_app(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    author = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    
    def __repr__(self):
        return f'<Book {self.title}>'
    
with app.app_context():
    db.create_all()
    
@app.route('/')
def home():
    
    # with app.app_context():
    all_books = db.session.execute(db.select(Book).order_by(Book.title)).scalars()
    print(all_books)
    return render_template('index.html', books = all_books)


@app.route("/add", methods = ['GET','POST'])
def add():
    if request.method == "POST":
        
        added_book = Book()
        added_book.title = request.form["book_name"]
        added_book.author = request.form["book_author"]
        added_book.rating = request.form["book_rating"]
        db.session.add(added_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')

@app.route('/edit/<int:book_id>', methods=['GET','POST'])
def change_rating(book_id):
    book_details = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    
    if request.method == 'GET':
        return render_template('book.html', book=book_details)
    elif request.method =='POST':
        new_rating = request.form["new_rating"]
        book_details.rating = new_rating
        db.session.commit()
        return redirect(url_for('home'))
        
@app.route('/delete/<int:book_id>',methods=['GET', 'POST'])
def delete_book(book_id):
    book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))
    
if __name__ == "__main__":
    app.run(debug=True)


