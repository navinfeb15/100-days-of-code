import csv
from flask_wtf import FlaskForm  
from flask_bootstrap import Bootstrap5
from wtforms.validators import DataRequired, URL
from flask import Flask, render_template, request, redirect, url_for
from wtforms import StringField, SubmitField, SelectField, BooleanField
from flask_sqlalchemy import SQLAlchemy

import os
os.chdir(r"C:\Users\2069852\OneDrive - Cognizant\Documents\python_files\100 days\100-days-of-code-main\Day-88")

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)
Bootstrap5(app)


class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=True)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)
    
    def to_dict(self):
        dictionary = {}
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)
        return dictionary

with app.app_context():
    db.create_all()
    
class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired(message="Please enter cafe name")])
    location_url = StringField('Location URL', validators=[DataRequired(), URL("Please enter a valid url")])
    image_url = StringField('Image URL', validators=[DataRequired(), URL("Please enter a valid url")])
    location = StringField('Cafe Location', validators=[DataRequired(message="Please enter cafe Location")])
    has_sockets = BooleanField('Has Sockets', default=False)
    has_toilet = BooleanField('Has Toilet', default=False)
    has_wifi = BooleanField('Has Wifi', default=False)
    can_take_calls = BooleanField('Can Take Calls', default=False)
    seats = StringField('Seats')
    coffee_price = StringField('Coffee Price', validators=[DataRequired()])
    submit = SubmitField('Submit')
    
@app.route("/")
def home():
    return render_template("index.html")

@app.route('/add', methods=['POST', 'GET'])  
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        new_cafe = Cafe(name=form.cafe.data,
                        map_url=form.location_url.data,
                        img_url=form.image_url.data,
                        location=form.location.data,
                        has_sockets=form.has_sockets.data == 'true',
                        has_toilet=form.has_toilet.data == 'true',
                        has_wifi=form.has_wifi.data == 'true',
                        can_take_calls=form.can_take_calls.data == 'true',
                        seats=form.seats.data,
                        coffee_price=form.coffee_price.data)
                        
        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for('cafes'))

    return render_template('add.html', form=form)

@app.route('/all')  
def cafes():
    all_cafes = db.session.execute(db.select(Cafe).order_by(Cafe.name)).scalars().all()
    list_of_rows = [cafe.to_dict() for cafe in all_cafes]
    return render_template('cafes_list.html', cafes=list_of_rows)

@app.route('/cafe/<int:cafe_id>', methods=['GET'])
def show_cafe(cafe_id):
    cafe_details = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
    return render_template("cafe_details.html", cafe_details=cafe_details)
  
if __name__ == '__main__':
    app.run(debug=True)