import time
from turtle import Screen
from car_manager import CarManager, cars_list,STARTING_MOVE_DISTANCE, MOVE_INCREMENT
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600,600)
screen.tracer(0)
screen.listen()

player = Player()
scoreboard = Scoreboard()
game_is_on = True

screen.onkeypress(fun=player.move_forward, key="Up")
screen.onkeypress(fun=player.move_backward, key="Down")

while game_is_on:
    time.sleep(0.1)
    cars_manager = CarManager()
    cars_manager.start_cars(distance=scoreboard.level)
    
    
    # collision = None
    # collision = car.check_collision(player_obj=player) 
    # if collision:
    #     player.reset_position()
    #     scoreboard.update_scoreboard()

    for car in cars_list:
        if car.distance(player) < 20:
            # player.reset_position()
            cars_manager.remove_cars()
            scoreboard.game_over()
            game_is_on = False
            
    
    if player.level_win():
        scoreboard.update_scoreboard()
        player.reset_position()
        # cars_manager.increase_speed()
            
    screen.update()
    
    

    # car.start_cars()
screen.exitonclick()
