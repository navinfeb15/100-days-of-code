from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(5, 1, 1)
        self.goto(position)

    def go_up(self):
        # Move the paddle up by 40 units on the y-axis
        y = self.ycor() + 40
        self.goto(self.xcor(), y)

    def go_down(self):
        # Move the paddle down by 40 units on the y-axis
        self.goto(self.xcor(), self.ycor() - 40)
