
# Cafe App

This is a simple Flask application for managing cafes and their information.

## Features

-   Add cafes with name, location, images, amenities etc.
-   View list of all added cafes
-   View detailed info for a specific cafe
-   Uses SQLite database to store cafe data
-   Utilizes Flask, Flask-SQLAlchemy, Flask-WTF for core functionality

## Setup

-   Install dependencies:
    -   Flask
    -   Flask-SQLAlchemy
    -   Flask-WTF
    -   Flask-Bootstrap
-   Setup database
    -   The app is configured to use SQLite database stored in  `cafes.db`
    -   Run  `python`  shell with app context to create the database:
        
        Copy code
        
        `from app import db db.create_all()`
        
-   Run the app
    -   `python app.py`
    -   Access the app at  [http://localhost:5000](http://localhost:5000/)

## Usage

-   Home page shows links to add a new cafe or view all cafes
-   Add Cafe page has form to enter cafe details like name, location etc.
-   View Cafes page lists all entered cafes
-   Can click on a cafe to see its detail page
-   Detail page shows all info for that cafe

## Structure

-   `app.py`  - Main Flask app code
-   `models.py`  - Database model for Cafe
-   `forms.py`  - Form using Flask-WTF
-   `templates/`  - HTML templates
-   `static/`  - Static assets

## Further Improvements

Some ways the app could be expanded:

-   User accounts/authentication
-   Allow editing/deleting cafes
-   Advanced search/filtering of cafes
-   Ratings/reviews for cafes
-   Integrate maps for cafe locations
-   Mobile-friendly responsive design
-   Deploy on production server


## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.