import random  # Import the random module

# Define the three hand gestures as string variables
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Create a list containing the three hand gestures
choice = [rock, paper, scissors]

# Prompt the user to input their choice and print the corresponding gesture
user_choice = int(input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if not user_choice > 2 or user_choice < 0:
    print("You chose\n", choice[user_choice])

    # Generate a random choice for the computer and print the corresponding gesture
    comp_choice = random.randint(0, 2)
    print("Computer chose:\n", choice[comp_choice])

    # Compare the user's choice with the computer's choice and print the result
    if user_choice == comp_choice:
        print("Match draw...")
    elif user_choice == 0:
        if comp_choice == 1:
            print("You Lose ☹️")
        elif comp_choice == 2:
            print("You Win !")
    elif user_choice == 1:
        if comp_choice == 0:
            print("You Win !")
        elif comp_choice == 2:
            print("You Lose ☹️")
    elif user_choice == 2:
        if comp_choice == 0:
            print("You Lose ☹️")
        elif comp_choice == 1:
            print("You Win !")
else:
    print("You entered an Invalid number. You lose.")
