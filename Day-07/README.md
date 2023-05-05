# Day-07
# Hangman

This is a Python script for playing the classic game of Hangman. The player must guess a hidden word by guessing one letter at a time, while being limited by a set number of incorrect guesses.

## How to Play

1. Clone the repository or download the `hangman.py` file.
2. Navigate to the `Day-07` folder.
3. Run the script using the `python hangman.py` command.
4. Follow the instructions on the screen to play the game.

## Game Description

The game of Hangman is a classic word-guessing game. In this implementation of the game, the player is presented with a hidden word, represented by a series of dashes. The player must guess one letter at a time, and if the letter is present in the word, the corresponding dashes are replaced with the letter. If the letter is not present in the word, the player is penalized with a wrong guess.

The player is limited by a set number of incorrect guesses, represented by the Hangman figure. If the player guesses the word correctly before the figure is completed, they win the game. If the Hangman figure is completed before the player guesses the word, they lose the game.

## Controls

The game is played entirely through the keyboard. The player must type a letter to make a guess.

## License

This script is licensed under the [MIT License](https://opensource.org/licenses/MIT).