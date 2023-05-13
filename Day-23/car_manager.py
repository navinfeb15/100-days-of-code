from turtle import Turtle
import random

COLORS = ["red","orange","yellow","blue","purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
cars_list = []

class CarManager():
    def __init__(self):
        # super().__init__()
        random_choice = random.randint(1, 6)
        if random_choice == 1:
            car = Turtle("square")
            car.color(random.choice(COLORS))
            car.shapesize(1,2,1)
            car.penup()
            # car.right(180)
            car.goto(300,random.randrange(-280,270))
            cars_list.append(car)

    def start_cars(self):
        for cars in cars_list:
            cars.back(STARTING_MOVE_DISTANCE)
