import time
from turtle import Screen
from car_manager import CarManager, cars_list, STARTING_MOVE_DISTANCE, MOVE_INCREMENT
from player import Player
from scoreboard import Scoreboard

# Set up the screen
screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
screen.listen()

# Create player, scoreboard, and initialize game variables
player = Player()
scoreboard = Scoreboard()
game_is_on = True

# Set up key bindings for player movement
screen.onkeypress(fun=player.move_forward, key="Up")
screen.onkeypress(fun=player.move_backward, key="Down")

while game_is_on:
    time.sleep(0.1)

    # Create and start car manager with distance based on scoreboard level
    cars_manager = CarManager()
    cars_manager.start_cars(distance=scoreboard.level)

    # Check for collision with player
    for car in cars_list:
        if car.distance(player) < 20:
            cars_manager.remove_cars()
            scoreboard.game_over()
            game_is_on = False

    # Check if player has reached the level win condition
    if player.level_win():
        scoreboard.update_scoreboard()
        player.reset_position()

    screen.update()

screen.exitonclick()
