import os
import hashlib
from datetime import date
from typing import Optional
from functools import wraps
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from wtforms.validators import DataRequired
from flask_ckeditor import CKEditor, CKEditorField
from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user,login_required

print(os.environ.get("SECRET_KEY"))
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("FLASK_KEY")
ckeditor = CKEditor(app)
Bootstrap5(app)

# Configure Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

# Connect to DB
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("URI", "sqlite:///posts.db")
db = SQLAlchemy()
db.init_app(app)

def get_gravatar_img(email: str):
    formatted_email = email.lower().strip()
    hex_value = hashlib.md5(formatted_email.encode()).hexdigest()
    result = f'https://www.gravatar.com/avatar/{hex_value}?d=retro'
    return result

# Configure Tables
class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.relationship("User", back_populates="user_posts")
    img_url = db.Column(db.String(250), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    comments = db.relationship('Comment', back_populates='parent_post')

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    user_posts = db.relationship('BlogPost', back_populates='author')
    comments = db.relationship('Comment', back_populates='comment_author')
    
    def is_active(self):
        return self.is_authenticated
    
    def get_id(self):
        return str(self.id)

class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(10000))    
    comment_author = db.relationship("User", back_populates='comments')
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    post_id = db.Column(db.Integer, db.ForeignKey('blog_posts.id'))
    parent_post = db.relationship("BlogPost", back_populates="comments")
    comment_author_name = db.Column(db.String(100)) 

with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id: str) -> Optional[User]:
    return User.query.get(int(user_id))

def restrict_route(func):
    @wraps(func)
    def restrict_wrapper(*args, **kwargs):
        # Perform some actions before the decorated function is called
        print("Before function execution")

        # Call the decorated function
        result = func(*args, **kwargs)

        # Perform some actions after the decorated function is called
        print("After function execution")

        # Return the result of the decorated function
        if current_user.get_id() == '1':
            return result
        else:
            return abort(403)

    # Return the wrapper function
    return restrict_wrapper

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    
    if form.validate_on_submit():
        if request.method == 'POST':
            matching_user = db.session.execute(db.select(User).where(User.email == form.email.data)).scalar()
            if matching_user:
                flash("You've already registered with that email. Please log in instead.")
                return redirect(url_for('login'))
            
            hashed_password = generate_password_hash(
                form.password.data,
                method='pbkdf2:sha256',
                salt_length=8
            )
            new_user = User(
                email=form.email.data,
                password=hashed_password,
                name=form.name.data
            )
            db.session.add(new_user)
            db.session.commit()
            
            login_user(new_user)
            return redirect(url_for('get_all_posts'))
        
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        if request.method == 'POST':
            user = User.query.filter_by(email=form.email.data).first()
            
            if user:
                if check_password_hash(user.password, form.password.data):
                    login_user(user)
                    return redirect(url_for('get_all_posts'))
                else:
                    flash('Password incorrect. Please try again.')
            else:
                flash('That email does not exist. Please try again.')
    
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))

@app.route('/')
def get_all_posts():
    posts = BlogPost.query.all()
    return render_template('index.html', all_posts=posts, current_user=current_user)

@app.route('/post/<int:post_id>', methods=['GET', 'POST'])
def show_post(post_id):
    form = CommentForm()
    requested_post = BlogPost.query.get(post_id)
    comments = Comment.query.filter_by(post_id=post_id).all()
    
    if form.validate_on_submit():
        if request.method == 'POST':
            if current_user.is_authenticated:
                new_comment = Comment(
                    text=form.comment_text.data,
                    comment_author=current_user,
                    parent_post=requested_post,
                    comment_author_name=current_user.name
                )
                db.session.add(new_comment)
                db.session.commit()
                return redirect(url_for('show_post', post_id=post_id))
            else:
                flash('You need to log in or register to comment.')
                return redirect(url_for('login'))
    
    return render_template('post.html', post=requested_post, form=form, comments=comments, current_user=current_user, get_img = get_gravatar_img)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/new-post', methods=['GET', 'POST'])
@login_required
@restrict_route
def add_new_post():
    form = CreatePostForm()
    
    if form.validate_on_submit():
        if request.method == 'POST':
            new_post = BlogPost(
                title=form.title.data,
                subtitle=form.subtitle.data,
                date=date.today().strftime("%B %d, %Y"),
                body=form.body.data,
                author=current_user,
                img_url=form.img_url.data
            )
            db.session.add(new_post)
            db.session.commit()
            return redirect(url_for('get_all_posts'))
    
    return render_template('make-post.html', form=form)

@app.route('/edit-post/<int:post_id>', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    post_to_edit = BlogPost.query.get(post_id)
    
    if post_to_edit.author != current_user:
        return abort(403)
    
    form = CreatePostForm(
        title=post_to_edit.title,
        subtitle=post_to_edit.subtitle,
        img_url=post_to_edit.img_url,
        body=post_to_edit.body
    )
    
    if form.validate_on_submit():
        if request.method == 'POST':
            post_to_edit.title = form.title.data
            post_to_edit.subtitle = form.subtitle.data
            post_to_edit.img_url = form.img_url.data
            post_to_edit.body = form.body.data
            db.session.commit()
            return redirect(url_for('show_post', post_id=post_id))
    
    return render_template('edit_post.html', form=form)

@app.route('/delete/<int:post_id>')
@login_required
def delete_post(post_id):
    post_to_delete = BlogPost.query.get(post_id)
    
    if post_to_delete.author != current_user:
        return abort(403)
    
    comments_to_delete = Comment.query.filter_by(post_id=post_id).all()
    
    for comment in comments_to_delete:
        db.session.delete(comment)
    
    db.session.delete(post_to_delete)
    db.session.commit()
    
    return redirect(url_for('get_all_posts'))

if __name__ == "__main__":
    app.run(debug=True, port=5002)