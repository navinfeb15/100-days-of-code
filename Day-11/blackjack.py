# This script plays a game of Blackjack
# The game is played between the user and the computer
# The user and the computer are each dealt two cards
# The user can choose to hit (get another card) or pass (not get another card)
# The goal is to get as close to 21 as possible without going over
# If either the user or the computer goes over 21, the other wins
# If both the user and the computer get 21, the user wins
import random
from art import logo


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Create empty lists to store the user and computer's cards
user_cards = []
computer_cards = []

# Set the game exit status to False
exit = False

# Function to add cards to the user's or computer's hand


def add_cards(player_cards: list, count):
    for times in range(count):
        player_cards.append(random.choice(cards))

# Function to check if the game is over


def check_over():
    if sum(user_cards) > 21:
        print("You went over. You lose 😭\n")
    elif sum(computer_cards) > 21:
        print("Opponent went over. You win 😊\n")

    if sum(user_cards) == 21:
        print("You win 😊\n")
    elif sum(computer_cards) == 21:
        print("You lose 😭\n")


# Start the game loop
while not exit:
    # Ask the user if they want to play a game of Blackjack
    play_again = input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n':")
    if play_again == 'y':
        print(logo)
        # Deal two cards to the user and the computer
        add_cards(user_cards, 2)
        add_cards(computer_cards, 2)

        # Keep playing until one of them has reached 21 or gone over
        while sum(user_cards) < 21 and sum(computer_cards) < 21:
            # Show the user their cards and the computer's first card
            print(
                f"  Your cards: {user_cards}, current score: {sum(user_cards)}")
            print(f"  Computer's first card: {computer_cards[0]}")
            # Ask the user if they want to hit or pass
            another_card = input(
                "Type 'y' to get another card, type 'n' to pass: ")
            if another_card == 'y':
                # Deal a card to the user and the computer
                add_cards(user_cards, 1)
                add_cards(computer_cards, 1)
                # Check if the game is over
                check_over()

            elif another_card == 'n':
                # Keep dealing cards to the computer until it reaches 21 or goes over
                while not sum(computer_cards) >= 21:
                    add_cards(computer_cards, 1)
                    # Check if the game is over
                    check_over()
        print(
            f"  your final hand: {user_cards}, final score: {sum(user_cards)}")
        print(
            f"  computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
        
        
    elif play_again == 'n':
        # Set the exit status to True to end the game loop
        exit = True
        print('\033[2J\033[H')
    else:
        print("Please enter a valid value ....\n")
