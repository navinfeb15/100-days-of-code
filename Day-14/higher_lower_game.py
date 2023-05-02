from art import logo, vs
from game_data import data
import random

# Print the logo
print(logo)

# Return a random person from the data


def random_person():
    return random.choice(data)

# Start the game


def game():
    # Initialize the current score
    current_score = 0

    # Loop until the game is over
    while True:
        # Get two random people
        celeb1 = random_person()
        celeb2 = random_person()
        # Print information about the first person
        print(
            f'Compare A:{celeb1["name"]}, a {celeb1["description"]}, from {celeb1["country"]}')
        # Print the vs symbol
        print(f"{vs}")
        # Print information about the second person
        print(
            f'Compare B:{celeb2["name"]}, a {celeb2["description"]}, from {celeb2["country"]}')

        # Determine which person has more followers
        popular = 'a' if celeb1["follower_count"] > celeb2["follower_count"] else 'b'
        # Ask the user to guess which person has more followers
        user_guess = input("Who has more followers? Type 'A' or 'B':").lower()

        # Check if the user's guess is correct
        if user_guess == popular:
            # Increase the score
            current_score += 1
            # Clear the screen
            print('\033[2J\033[H')
            # Print the current score
            print(f"You're right! Current score: {current_score}")

        else:
            # Print the final score
            print(f"Sorry, that's wrong. Final score: {current_score}")
            # End the game
            return


# Start the game
game()
