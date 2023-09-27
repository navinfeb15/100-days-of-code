import numpy as np
import os

# Global variable to determine if the players want to play again
global play_again
play_again = True

# Function for player 1's move
def player1_move(moves):
    user_1_pos = int(input("Player 1, Choose your position\n"))
    row_pos = (user_1_pos-1)//3

    # Calculate the column position
    while user_1_pos > 3:
        user_1_pos -= 3
    col_pos = user_1_pos - 1

    # Check if the board is full
    if moves > 9:
        print("Board Filled. Game Draw!!!")
        rematch()

    # Check if the chosen position is valid and not occupied by player 2
    elif t[row_pos][col_pos] != user_2 and t[row_pos][col_pos] != user_1:
        t[row_pos][col_pos] = user_1
        moves += 1
    else:
        print("Position already occupied by player 2!!!")
        show_board()
        player1_move(move_count)

# Function for player 2's move
def player2_move(moves):
    user_2_pos = int(input("Player 2, Choose your position\n"))
    row_pos = (user_2_pos-1)//3
    while user_2_pos > 3:
        user_2_pos -= 3
    col_pos = user_2_pos - 1

    # Check if the board is full
    if moves > 9:
        print("Board Filled. Game Draw!!!")
        rematch()

    # Check if the chosen position is valid and not occupied by player 1
    elif t[row_pos][col_pos] != user_1 and t[row_pos][col_pos] != user_2:
        t[row_pos][col_pos] = user_2
        moves += 1
    else:
        print("Position already occupied by player 1!!!")
        show_board()
        player2_move(move_count)

# Function to check for a win
def check_for_win(table):
    show_board()
    # Check if rows are equal
    for row in table:
        first_elem = row[0]
        if (row == first_elem).all() and first_elem != " ":
            print(f"{first_elem.upper()} Wins ny row")
            rematch()
            return first_elem.upper()

    # Check if columns are equal
    for col in range(0, 3):
        first_elem = table[0][col]
        if table[1][col] == first_elem and table[2][col] == first_elem and first_elem != " ":
            print("Win")
            print(f"{first_elem.upper()} Wins by column")
            rematch()
            return first_elem.upper()

    # Check if diagonals are equal
    first_elem = table[0][0]
    last_elem = table[0][-1]
    if table[1][1] == first_elem and table[2][2] == first_elem and first_elem != " ":
        print(f"{first_elem.upper()} Wins by diagonal")
        rematch()
        return first_elem.upper()
    elif table[1][1] == last_elem and table[2][0] == last_elem and last_elem != " ":

        print(f"{last_elem.upper()} Wins by diagonal")
        rematch()
        return last_elem.upper()

    return False

# Function to ask for a rematch
def rematch():
    global play_again
    new_match = input("Do you want to play another game (Y/N)\n")
    if new_match.lower() == 'y':
        os.system('cls')
        play_again = True
    else:
        play_again = False

# Main game loop
while play_again:
    # Initialize variables
    move_count = 0

    t = np.array([[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])

    # Function to display the game board
    def show_board():
        for row in range(0, 3):
            print(f"{t[row][0]} | {t[row][1]} | {t[row][2]}")
            print("-- --- --") if row != 2 else None
        print("\n")

    print("Welcome to Tic-Tac-Toe")
    user_1 = input("Player 1, Please Choose your Marker (X, O, or any other character)\n😉")
    user_2 = input("Player 2, Please Choose your Marker (X, O, or any other character)\n😉")
    print("Readyto play? Please enter your feasible position to place your marker from the structure below...")
    for num in range(1, 8, 3):
        print(num, num + 1, num + 2)
    print("\nBoard : ")

    show_board()
    while True:
        player1_move(move_count)
        if check_for_win(t):
            break
        player2_move(move_count)

        if check_for_win(t):
            break