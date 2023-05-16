## Day-25

# U.S. States Game

This Python program is a game that tests your knowledge of U.S. states. It uses the turtle graphics library to display an interactive map of the United States, where the user can guess the names of the states by clicking on their locations. The program keeps track of the user's score and provides feedback on correct and incorrect guesses.

## Requirements

To run this program, you need the following:

-   Python 3.x
-   Turtle graphics library
-   Pandas library

## Installation

1.  Clone the repository or download the source code files.
    
2.  Install the required libraries by running the following command:
    
    bashCopy code
    
    `pip install pandas turtle` 
    

## Usage

1.  Make sure you have the "50_states.csv" file, which contains the data of all 50 U.S. states and their coordinates.
    
2.  Run the program using the following command:
    
    bashCopy code
    
    `python us_states_game.py` 
    
3.  A window will open displaying the map of the United States. The program will prompt you to guess the names of the states.
    
4.  Type the name of a state and press Enter to make a guess. If your guess is correct, the program will display the name of the state at its location on the map.
    
5.  Continue guessing the names of the states until you have correctly guessed all 50 states or choose to exit by typing "Exit" when prompted.
    
6.  After exiting the game, a CSV file named "states_to_learn.csv" will be generated, which contains the names of the states that you didn't guess correctly. This file can be used for further learning and practice.
    

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
