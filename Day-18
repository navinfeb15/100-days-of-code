import turtle as t
from turtle import Turtle, Screen
import random

# List of colors in RGB format
color_list = [(207, 160, 82), (54, 88, 130), (145, 91, 40), (140, 26, 49), (221, 207, 105), (132, 177, 203),
              (158, 46, 83), (45, 55, 104), (169, 160, 39), (129, 189, 143), (83, 20, 44), (37, 43, 67),
              (186, 94, 107), (187, 140, 170), (85, 120, 180), (59, 39, 31), (88, 157, 92), (78, 153, 165),
              (194, 79, 73), (45, 74, 78), (80, 74, 44), (161, 201, 218), (57, 125, 121), (219, 175, 187),
              (169, 206, 172), (219, 182, 169)]

# Create a turtle named "timmy"
timmy = Turtle()

# Set the color mode to 255
t.colormode(255)

# Hide the turtle and lift the pen up
timmy.hideturtle()
timmy.penup()

# Position the turtle to start drawing in the bottom left corner of the screen
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)

starting_x = timmy.xcor()
starting_y = timmy.ycor()

# Define a function to draw the Hirst painting
def hirst(num):
    # Draw num rows of dots
    for __ in range(1, num+1):
        # Draw num dots in each row
        for _ in range(num):
            # Choose a random color and draw a dot
            timmy.dot(20, random.choice(color_list))
            timmy.forward(50)
        # Move the turtle to the beginning of the next row
        timmy.goto(starting_x, starting_y + 50*__)

# Call the hirst function to draw the painting with 10 rows and columns of dots
hirst(10)

# Create a screen and wait for the user to click before closing it
screen = Screen()
screen.exitonclick()
