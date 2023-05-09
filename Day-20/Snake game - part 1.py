from turtle import Turtle, Screen
import random
import time
from snake import Snake

# Initialize the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")

# Turn off animation to speed up the game
screen.tracer(0)

# Initialize the game
game_on = True
snake = Snake()

# Listen for keyboard input
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

# Start the game loop
while game_on:
    # Move the snake
    snake.move()
    time.sleep(0.5)
    screen.update()

# Exit the game when the user clicks the screen
screen.exitonclick()