import random
from art import logo

# Prints the logo
print(logo)

# Introduces the game
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

# Generates a random number
number = random.randint(1, 100)

# Asks the user to choose a difficulty
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

# Defines the guessing function


def guess(num, chances):
    user_guess = 0
    while user_guess != num:
        print(f"You have {chances} attempts remaining to guess the number")
        user_guess = int(input("Make a guess: "))
        if user_guess > num:
            print("Too high.\nGuess again.")
        elif user_guess < num:
            print("Too low.\nGuess again.")
        else:
            print(f"You got it! The answer was {num}.")
            return
        chances -= 1
        if chances == 0:
            print("You've run out of guesses, you lose.")
            return

# Sets the difficulty level
if difficulty.lower() == "hard":
    guess(number, 5)
elif difficulty.lower() == "easy":
    guess(number, 10)
else:
    print("please choose correct difficulty.")
