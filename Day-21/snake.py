from turtle import Turtle, Screen  # Import the Turtle and Screen classes
import random  # Import the random module
import time  # Import the time module

# Define some constants
TURTLE_LENGTH = 3  # The length of the snake when it starts
MOVE_DISTANCE = 20  # The distance the snake moves each time
UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0  # The heading directions

class Snake:
    def __init__(self):
        self.segments = []  # Initialize an empty list to hold the snake's segments
        self.create_snake()  # Call the create_snake method to create the snake
        self.head = self.segments[0]  # Get the head of the snake

    def create_snake(self):
        for i in range(0, TURTLE_LENGTH):
            self.add_segment()

    def add_segment(self):
        # Create a new Turtle object for the segment
        turtle = Turtle(shape="square")
        turtle.color("white")
        turtle.penup()

        # Position the new segment behind the last one in the list
        if self.segments:
            turtle_xcor = self.segments[-1].xcor()
            turtle.setpos(turtle_xcor - 20, 0)

        # Add the new segment to the list of segments
        self.segments.append(turtle)

    def move(self):
        # Move each segment to the position of the segment in front of it
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x, new_y)

        # Move the head of the snake forward by the MOVE_DISTANCE
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:  # Make sure the snake isn't moving down
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:  # Make sure the snake isn't moving up
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:  # Make sure the snake isn't moving right
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:  # Make sure the snake isn't moving left
            self.head.setheading(RIGHT)

    def wall_collision(self):
        # Check if the head of the snake has collided with a wall
        if (
            self.head.xcor() >= 300
            or self.head.xcor() <= -300
            or self.head.ycor() >= 300
            or self.head.ycor() <= -300
        ):
            return True

    def tail_collision(self):
        # Check if the head of the snake has collided with its tail
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                return True
            else:
                return False
