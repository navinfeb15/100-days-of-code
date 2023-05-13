from turtle import Turtle

STARTING_POSITION = (0,-200)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 200

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def move_backward(self):
        self.back(MOVE_DISTANCE)


