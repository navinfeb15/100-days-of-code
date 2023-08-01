
## Day-63
# Books Collection Flask App

This is a simple Flask web application for managing a collection of books. Users can add new books, edit book ratings, and delete books from the collection. The application uses SQLAlchemy to interact with a SQLite database to store book information.

## Getting Started

These instructions will help you set up and run the application on your local machine.

### Prerequisites

- Python (version 3.6 or higher)
- pip (Python package installer)
- Virtual environment (optional but recommended)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/navinfeb15/100-days-of-code.git
   cd books-collection-flask-app
   ```

2. Create and activate a virtual environment (recommended):

   ```bash
   # Create a virtual environment
   python -m venv venv

   # Activate the virtual environment
   # On Windows
   venv\Scripts\activate
   # On macOS and Linux
   source venv/bin/activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Run the application:

   ```bash
   python app.py
   ```

2. Open a web browser and navigate to `http://127.0.0.1:5000/` to access the application.

3. Use the provided web interface to manage your collection of books.

### Features

- View the list of all books in the collection on the homepage.
- Add new books to the collection by providing title, author, and rating.
- Edit the rating of a book by navigating to the edit page.
- Delete books from the collection.

## Built With

- Flask - Web framework
- SQLAlchemy - Database toolkit
- HTML/CSS - Front-end design

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
