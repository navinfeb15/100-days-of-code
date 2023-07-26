import csv
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap5
from wtforms.validators import DataRequired, URL
from flask import Flask, render_template, request
from wtforms import StringField, SubmitField, TimeField, SelectField

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[
                       DataRequired(message="Please enter cafe name")])
    location = StringField('Location URL',  validators=[
                           DataRequired(), URL("Please enter a valid url")])
    open_time = StringField('Opening Time')
    close_time = StringField('Closing Time')
    coffee_rating = SelectField('Coffee Rating', choices=[(
        1, '☕'), (2, '☕️☕️'), (3, '☕️☕️☕️'), (4, '☕️☕️☕️☕️'), (5, '☕️☕️☕️☕️☕️')])
    wifi_rating = SelectField('Wifi Rating', choices=[(
        1, '✘'), (2, '✘✘'), (3, '✘✘✘'), (4, '✘✘✘✘'), (5, '✘✘✘✘✘')])
    outlet_rating = SelectField('Power Outlet Rating', choices=[(
        1, '🔌'), (2, '🔌🔌'), (3, '🔌🔌🔌'), (4, '🔌🔌🔌🔌'), (5, '🔌🔌🔌🔌🔌')])
    submit = SubmitField('Submit')


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['POST', 'GET'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
        with open('cafe-data.csv', mode='a+', encoding='utf-8') as csv_file:
            # csv_data = csv.writer(csv_file, delimiter=',')
            cafe_data = f'\n{request.form["location"]},{request.form["open_time"]},{request.form["close_time"]},{int(request.form["coffee_rating"])*"☕"},{int(request.form["wifi_rating"])*"✘"},{int(request.form["outlet_rating"])*"🔌"}'
            csv_file.writelines(cafe_data)

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
