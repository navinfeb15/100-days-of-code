from flask import Flask
import random

# Generate a random number between 0 and 9
random_num = random.randint(0, 9)

# Create a Flask application
app = Flask(__name__)


# Decorator function to wrap the output with <h1> tags
def make_h1(function):
    def wrapper():
        return "<h1>" + function() + "</h1>"
    return wrapper


# Route for the home page
@app.route("/")
@make_h1
def welcome():
    # Display a welcome message and an image
    return "Guess a number between 0 and 9 <br><br><br>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' height=200 width=200>"


# Route to check the guessed number against the random number
@app.route("/<int:number>")
def check_num(number):
    if number == random_num:

        # If the guessed number is correct, display a success message in red color
        return f"<h1 style='color: red;'>Yay! You found me!.</h1><br><br>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' height=500 width=500>"

    elif number < random_num:

        # If the guessed number is too low, display a message in blue color
        return f"<h1 style='color: blue;'> Too low, try again!</h1><br><br>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' height=500 width=500>"

    elif number > random_num:

        # If the guessed number is too high, display a message in green color
        return f"<h1 style='color: green;'> Too high, try again!</h1><br><br>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' height=500 width=500>"


# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
