from turtle import Turtle

STARTING_POSITION = (0,-280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.reset_position()
        self.left(90)

    def reset_position(self):
        self.goto(STARTING_POSITION)

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def move_backward(self):
        self.back(MOVE_DISTANCE)

    def level_win(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False


