## Day-62

# Flask Cafe App

This is a simple Flask application for managing and displaying cafe information. It allows users to add cafes with their details such as name, location, opening and closing times, and ratings for coffee, wifi, and power outlets. The data is stored in a CSV file and can be viewed on the website.

## Prerequisites

Make sure you have the following installed:

-   Python 3.x
-   Flask
-   Flask-WTF
-   Flask-Bootstrap

## Getting Started

1.  Clone the repository or download the source code.
    
2.  Install the required dependencies by running the following command in your terminal:
    
    ```
    pip install flask flask_wtf flask_bootstrap
    ```
    
3.  Run the Flask application by executing the following command:
    

    
    ```
    python app.py    
    ```
    
4.  Open your web browser and visit  `http://localhost:5000`  to access the application.
    

## Usage

### Home Page

-   The home page displays a welcome message and provides navigation links to other sections of the application.

### Add Cafe

-   Click on the "Add Cafe" link in the navigation menu to add a new cafe.
-   Fill in the required fields such as cafe name, location URL, opening time, closing time, and ratings.
-   Click the "Submit" button to save the cafe information.
-   The data will be stored in the  `cafe-data.csv`  file.

### View Cafes

-   Click on the "Cafes" link in the navigation menu to view the list of cafes.
-   The cafes are displayed in a tabular format, showing their names, locations, opening times, closing times, coffee ratings, wifi ratings, and power outlet ratings.
-   The cafe data is read from the  `cafe-data.csv`  file.

## File Structure

-   `app.py`: The main Flask application file containing the routes and logic.
-   `templates/`: This directory contains the HTML templates used by the Flask application.
    -   `index.html`: The home page template.
    -   `add.html`: The template for adding a new cafe.
    -   `cafes.html`: The template for displaying the list of cafes.
-   `cafe-data.csv`: The CSV file used to store the cafe data.

## Contributing

Contributions are welcome! If you find any issues or want to add new features, please submit a pull request or open an issue on the GitHub repository.

## License

This project is licensed under Free [MIT License](LICENSE). Feel free to use and modify the code for your own purposes.