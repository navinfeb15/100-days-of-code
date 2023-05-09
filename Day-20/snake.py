from turtle import Turtle,Screen
import random, time

TURTLE_LENGTH = 3
MOVE_DISTANCE = 20
UP,DOWN,LEFT,RIGHT = 90,270,180,0

class Snake:
    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(0,TURTLE_LENGTH):
            turtle = Turtle(shape="square")
            turtle_xcor = turtle.xcor()
            turtle.color("white")
            turtle.penup()
            # if i > 0:
            turtle.setpos(turtle_xcor-20*i,0)
            self.segments.append(turtle)
            # print(turtle[i].pos())

    def move(self):
        for segment in range(len(self.segments)-1,0,-1):
            # print(segment)
            new_x = self.segments[segment-1].xcor()
            new_y = self.segments[segment-1].ycor()

            self.segments[segment].goto(new_x,new_y)
        
        self.head.forward(MOVE_DISTANCE)

        # self.turtles[0].right(90)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
