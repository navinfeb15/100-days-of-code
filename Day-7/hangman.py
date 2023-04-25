from hangman_art import logo, stages
from hangman_words import word_list
import random


# Choose a random word from the word list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# Print the game logo
print(logo)

# Create a list of underscores to represent the word
display = []
for _ in range(word_length):
    display += "_"

# Loop until the game ends
while not end_of_game:
    # Get user input for a letter guess
    guess = input("Guess a letter: ").lower()

    # Check if the letter has already been guessed
    if guess in display:
        print("You've already guessed it : " + guess)

    # Replace underscores with the guessed letter if it is in the word
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # If the guessed letter is not in the word, lose a life
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in a word. you lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose. The word is {chosen_word}")

    # Print the current state of the word
    print(f"{' '.join(display)}")

    # Check if the user has won
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # Print the current state of the hangman
    print(stages[lives])

