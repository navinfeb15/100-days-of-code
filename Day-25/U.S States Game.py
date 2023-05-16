import turtle

import pandas as pd

# Read the CSV file
states_df = pd.read_csv(r"Day-25/50_states.csv")

# Create a turtle screen
screen = turtle.Screen()
screen.title("U.S. States Game")

# Set the background image
image = "Day-25\\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle.penup()

# Initialize variables
correct_guess = []
state_to_learn = []
score = 0

# Game loop
while len(correct_guess) < 50:
    # Prompt for the state's name
    answer_state = screen.textinput(title=str(score) + "/50 States Correct",
                                    prompt="What's another state's name?")

    if answer_state == "Exit":
        break

    # Get coordinates of the answer state
    coordinates = states_df[states_df.state == answer_state.title()]

    if not coordinates.empty:
        # Increase the score
        score += 1

        # Create a new turtle for the answer state
        new_t = turtle.Turtle()
        new_t.penup()
        new_t.hideturtle()

        # Move the turtle to the corresponding coordinates
        new_t.goto(int(coordinates.x), int(coordinates.y))

        # Write the state's name on the screen
        new_t.write(arg=coordinates.state.values[0], align="center")

        # Add the correct guess to the list
        correct_guess.append(coordinates.state.values[0])

# Find states to learn
states_to_learn = states_df[~states_df.state.isin(correct_guess)]

# Save states to learn in a CSV file
states_to_learn.to_csv("Day-25\\states_to_learn.csv")

# Close the turtle screen when clicked
screen.exitonclick()
