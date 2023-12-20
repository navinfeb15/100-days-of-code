from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from wtforms import StringField, SubmitField, SelectField
from flask_wtf import FlaskForm  
from wtforms.validators import DataRequired
from wtforms.fields import DateField
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_wtf.csrf import CSRFProtect
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy()
db.init_app(app)

class Task_model(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(250))  
    priority = db.Column(db.String(50))
    date = db.Column(db.DateTime)
    
with app.app_context():
    db.create_all()
    
class TaskForm(FlaskForm):
    task = StringField('Task', validators=[DataRequired()])
    priority = SelectField('Priority', choices=[('lp', 'Low Priority'), ('mp', 'Medium Priority'), ('hp', 'High Priority')])
    date = DateField('Date', format='%Y-%m-%d', default=datetime.now(), validators=[DataRequired()])
    submit = SubmitField('Save Task')

@app.route("/", methods=['POST', 'GET'])  
def home_page():
    form = TaskForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_task = Task_model(
                task=form.task.data,
                priority=form.priority.data, 
                date=form.date.data
            )
            
            db.session.add(new_task)
            db.session.commit()
            return redirect(url_for('home_page'))
            
    if request.method == 'GET':
        form.task.data = request.form.get('task')
        form.priority.data = request.form.get('priority')
        form.date.data = request.form.get('date')
        
    all_tasks = db.session.execute(db.select(Task_model)).scalars().all()
    for tasks in all_tasks:
        tasks.date = tasks.date.strftime("%d-%m-%Y")
        
    return render_template("index.html", task_form=form, task_list=all_tasks)

@app.route("/del/<int:task_id>", methods=["GET"])
def del_task(task_id):
    task_details = db.session.execute(db.select(Task_model).where(Task_model.id == task_id)).scalar()
    db.session.delete(task_details)
    db.session.commit()
    return redirect(url_for('home_page'))

@app.route("/complete/<int:task_id>", methods=["GET"])   
def complete_task(task_id):
    task_details = db.session.execute(db.select(Task_model).where(Task_model.id == task_id)).scalar()
    task_text = task_details.task
    task_details.task = '\u0336'.join(task_text) + '\u0336'
    
    db.session.commit()
    return redirect(url_for('home_page'))
    
if __name__ == '__main__':
    app.run()