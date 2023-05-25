from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "blue", "purple"]

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
cars_list = []

class CarManager():
    def __init__(self):
        random_choice = random.randint(1, 6)
        
        if random_choice == 1:
            # Create a car
            car = Turtle("square")
            car.color(random.choice(COLORS))
            car.shapesize(1, 2, 1)
            car.penup()
            car.goto(300, random.randrange(-260, 260))
            cars_list.append(car)

    def start_cars(self, distance=0):
        for car in cars_list:
            # Move the cars based on the starting move distance plus distance parameter
            car.back(STARTING_MOVE_DISTANCE + 10 * distance)
    
    def increase_speed(self):
        # Increase the starting move distance by the move increment
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT            

    def check_collision(self, player_obj):
        for car in cars_list:
            if car.distance(player_obj) < 20:
                return True
        return False
    
    def remove_cars(self):
        for car in cars_list:
            car.hideturtle()
