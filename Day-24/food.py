from turtle import Turtle  # Import the Turtle class
import random  # Import the random module

class Food(Turtle): 
    def __init__(self):
        super().__init__()  # Call the parent class constructor

        # Set up the food Turtle object
        self.shape("square")  # Set the shape of the food to a square
        self.penup()  # Lift the pen up so it doesn't draw lines
        self.color("yellow")  # Set the color of the food to yellow
        self.shapesize(0.5,0.5)  # Set the size of the food
        self.speed("fastest")  # Set the animation speed of the food
        self.refresh()  # Move the food to a random location on the screen

    def refresh(self):
        random_x = random.randint(-280, 280)  # Generate a random x-coordinate
        random_y = random.randint(-280, 280)  # Generate a random y-coordinate
        self.goto(random_x,random_y)  # Move the food to the random coordinates
