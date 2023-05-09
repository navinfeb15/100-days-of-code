from turtle import Turtle, Screen
import random

# Setup the screen
screen = Screen()
screen.setup(width=600, height=600)

# Get the user's choice of turtle color
user_choice = screen.textinput(
    "Turtle Racing", "Choose the color of turtle you want to bet on:")

# List of possible turtle colors
colors = ['red', 'blue', 'yellow', 'green', 'orange', 'purple']

# List of Race objects
turtles_list = []

# Flag to track if the game is still on
is_game_on = False

# Count of the number of turtles
turtle_count = 0

# Race class to define the attributes of the turtle


class Race():

    # Initialize the Race object
    def __init__(self, turtle_color):
        self.turtle_color = turtle_color
        self.turtle = Turtle(shape="turtle")

        self.turtle.color(turtle_color)
        self.turtle.penup()

        global turtle_count
        turtle_count += 1
        self.goto_xy = (-280, 90 - 30*turtle_count)

    # Set the turtle's position
    def set_position(self, pos):
        self.turtle.goto(pos)

    # Move the turtle forward
    def forward(self, distance):
        self.turtle.forward(distance)

    # Get the turtle's x coordinate
    def xcor(self):
        return self.turtle.xcor()


# Start the game if the user has chosen a color
if user_choice:
    is_game_on = True

    # Create a Race object for each color
    for color in colors:
        turtle_name = str(color) + "_turtle"
        turtle_name = Race(color)
        # print(color,":", turtle_name.goto_xy)

        # Set the turtle's position
        turtle_name.set_position(turtle_name.goto_xy)
        turtles_list.append(turtle_name)

    # Keep looping until one of the turtles has reached the end of the race
    while is_game_on:

        # Loop through each turtle
        for turtle in turtles_list:
            # Check if the turtle has reached the end of the race
            if turtle.xcor() >= 265:
                # print(turtle.xcor())
                is_game_on = False

                # Check if the user's choice of turtle won
                if user_choice == turtle.turtle_color:
                    print(f"You won! The {turtle.turtle_color} won the Race ")
                    # is_game_on=False
                else:
                    print(f"You Lost! The {turtle.turtle_color} won the Race ")
                break

            # Move the turtle forward a random distance
            dist = random.randint(0, 10)
            turtle.forward(dist)

# Exit the screen
screen.exitonclick()
