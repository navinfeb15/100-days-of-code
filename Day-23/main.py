import time
from turtle import Screen
from car_manager import CarManager
from player import Player


player = Player()

screen = Screen()
screen.setup(600,600)
screen.tracer(0)
screen.listen()
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    
    car = CarManager()
    car.start_cars()
    screen.update()

    screen.onkeypress(fun=player.move_forward, key="Up")
    screen.onkeypress(fun=player.move_backward, key="Down")

    # car.start_cars()
    
