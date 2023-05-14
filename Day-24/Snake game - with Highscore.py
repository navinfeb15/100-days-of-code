from turtle import Turtle, Screen
import random
import time
from snake import Snake  # Import the Snake class from snake.py
from food import Food  # Import the Food class from food.py
from scoreboard import ScoreBoard  # Import the ScoreBoard class from scoreboard.py

# Initialize the screen
screen = Screen()
screen.setup(width=600, height=600)  # Set the screen size
screen.bgcolor("black")  # Set the screen background color

# Turn off animation to speed up the game
screen.tracer(0)

# Initialize the game
game_on = True
snake = Snake()  # Create a new Snake object
food = Food()  # Create a new Food object
score = ScoreBoard()  # Create a new ScoreBoard object

# Listen for keyboard input
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

# Start the game loop
while game_on:
    # Move the snake
    snake.move()  # Move the snake forward
    time.sleep(0.1)  # Pause for a moment to slow down the game
    screen.update()  # Update the screen

    # Check for collision with food
    if snake.head.distance(food) < 15:  # If the snake's head is close to the food
        score.add_score()  # Increase the score
        snake.add_segment()  # Add a new segment to the snake
        food.refresh()  # Move the food to a new random location

    # Check for collision with the wall
    if snake.wall_collision():  # If the snake collides with the wall
        # score.game_over()  # Show the game over message
        # game_on = False  # End the game loop
        score.reset()
        snake.reset()


    # Check for collision with the tail
    if snake.tail_collision():  # If the snake collides with its own tail
        # score.game_over()  # Show the game over message
        # game_on = False  # End the game loop
        score.reset()
        snake.reset()

# Exit the game when the user clicks the screen
screen.exitonclick()
