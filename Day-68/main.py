from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
import werkzeug
import os


# Create the Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR-SECRET-KEY'

# Connect to the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy()

# Initialize the login manager
login_manager = LoginManager()
login_manager.init_app(app)
db.init_app(app)

# Define the User model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

    def is_active(self):
        return self.is_authenticated

    def get_id(self):
        return str(self.id)

# Create the database tables
with app.app_context():
    db.create_all()

# Load the user for the login manager
@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

# Home route
@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)

# Register route
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == "POST":
        # Create a new user
        user_to_add = User(
            email=request.form['email'],
            password=werkzeug.security.generate_password_hash(request.form['password'], method='pbkdf2:sha256', salt_length=8),
            name=request.form['name']
        )
        
        # Check if the user already exists
        existing_user = db.session.execute(db.select(User).where(User.email == request.form['email'])).scalar()
        if existing_user:
            flash("You have already registered using that email. Log in instead.")
            return redirect(url_for('login'))
        
        # Add the user to the database
        db.session.add(user_to_add)
        db.session.commit()
        return redirect(url_for('login'))
    
    return render_template("register.html", logged_in=current_user.is_authenticated)

# Login route
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method =='POST':
        # Retrieve the user from the database
        user = User.query.filter_by(email=request.form.get("email")).first()

        if user:
            # Check if the password is correct
            if werkzeug.security.check_password_hash(user.password, request.form['password']):
                login_user(user)
                return redirect(url_for("secrets", name=user.name))
            else:
                flash("Password Incorrect. Please try again")
        else:
            flash("This email does not exist. Please try again")
            
    return render_template("login.html", logged_in=current_user.is_authenticated)

# Secrets route
@app.route('/secrets')
@login_required
def secrets():
    name = request.args.get("name")
    return render_template("secrets.html", newuser_name=name, logged_in=current_user.is_authenticated)

# Logout route
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

# Download route
@app.route('/download', methods=['GET', 'POST'])
@login_required
def download():
    return send_from_directory('static', path="files/cheat_sheet.pdf")

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
