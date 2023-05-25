from turtle import Turtle
import random

COLORS = ["red","orange","yellow","blue","purple"]

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
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
            car.goto(300,random.randrange(-260,260))
            cars_list.append(car)

    def start_cars(self, distance = 0):
        for cars in cars_list:
            cars.back(STARTING_MOVE_DISTANCE + 10 * distance)
    
    def increase_speed(self):
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT            

    def check_collision(self, player_obj):
        for cars in cars_list:
            # if player_obj.distance(cars) < 20 and player_obj.ycor() < cars.ycor(): #player hit car
            #     print("collision")
            #     return True
            # if player_obj.distance(cars) < 30 and player_obj.ycor() +15 >=  cars.ycor(): #car hit player
            #     print("collision")
            if cars.distance(player_obj) < 20:
                return True
            else:
                return False
            # elif player_obj.distance(cars) < 30 and player_obj.ycor() < cars.ycor()-10:
            #     print("collision")
    def remove_cars(self):
        for cars in cars_list:
            cars.hideturtle()
