
# Flask Todo App

This is a simple todo app built with Flask and SQLite.

## Overview

The app allows users to:

-   Add new tasks
-   Set priority (high, medium, low) and due date
-   Mark tasks as completed
-   Delete tasks

The tasks are saved in an SQLite database `tasks.db`.

## Setup

### Dependencies

-   Flask
-   Flask-SQLAlchemy
-   Flask-WTF
-   Flask-Bootstrap

Install dependencies:

Copy code

`pip install flask flask-sqlalchemy flask-wtf flask-bootstrap`

### Config

The SQLite database is configured in `app.py`:

python

Copy code

`app.config['SQLALCHEMY_DATABASE_URI']  =  'sqlite:///tasks.db'`

A secret key is also required in `app.py` for the Flask app instance.

### Running the App

To run the app:

Copy code

`python app.py`

The app will be served at `http://localhost:5000`

## Code Overview

**app.py**

This contains the Flask application instance and routes.

The main route `"/"` handles displaying the tasks and adding new tasks.

**models.py**

Contains the SQLAlchemy model for the Task database table.

**forms.py**

Defines the WTForm classes for the add/edit task form.

**Templates**

The `index.html` template generates the main tasks page.

## Further Improvements

Some ideas for enhancements:

-   Add user accounts
-   Edit existing tasks
-   Search/filter tasks
-   Categorize tasks into projects
-   Status for tasks in progress
## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.