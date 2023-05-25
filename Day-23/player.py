from turtle import Turtle

STARTING_POSITION = (0, -280)
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
        # Reset the player's position to the starting position
        self.goto(STARTING_POSITION)

    def move_forward(self):
        # Move the player forward by the move distance
        self.forward(MOVE_DISTANCE)

    def move_backward(self):
        # Move the player backward by the move distance
        self.back(MOVE_DISTANCE)

    def level_win(self):
        # Check if the player has reached the finish line
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
