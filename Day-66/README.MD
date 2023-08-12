## Day-66

# Flask Cafe App



This project is part of the "100 Days of Code" challenge. It is a Flask application that provides an API to manage information about cafes. The application uses SQLite as the database and allows creating, reading, updating, and deleting cafe records.

## Prerequisites

-   Python 3.x
-   Flask
-   Flask SQLAlchemy

## Installation

1.  Clone the repository:  `git clone https://github.com/<your-username>/100-days-of-code.git`
2.  Change to the project directory:  `cd 100-days-of-code/Day-66`
3.  Install the dependencies:  `pip install -r requirements.txt`

## Usage

1.  Set up the SQLite database by running  `python app.py`  in the project directory.
2.  Access the API routes using your preferred HTTP client.

## API Routes

1.  GET /random - Returns information about a random cafe from the database.
2.  GET /all - Returns information about all cafes in the database.
3.  GET /search - Returns information about cafes that match the specified location.
4.  POST /add - Adds a new cafe to the database.
5.  PATCH /update-price/{cafe_id} - Updates the price of a cafe with the specified ID.
6.  DELETE /report-closed/{cafe_id} - Deletes a cafe with the specified ID from the database.

Please refer to the code comments and the API routes' documentation for more details on how to use the routes.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to submit a pull request.


## License

This project is licensed under Free [MIT License](LICENSE). Feel free to use and modify the code for your own purposes.