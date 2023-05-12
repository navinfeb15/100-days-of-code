from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.goto(0, 0)
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move_ball(self):
        # Move the ball based on its x and y movements
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_y(self):
        # Bounce the ball if it hits the upper wall or the lower wall
        if self.ycor() > 290:
            self.y_move *= -1
        elif self.ycor() < -280:
            self.y_move *= -1

    def bounce_x(self):
        # Bounce the ball if it hits a paddle, and increase its speed
        self.x_move *= -1
        self.ball_speed *= 0.9

    def right_paddle_miss(self):
        # Check if the ball misses the right paddle and returns True if it does, otherwise False
        if self.xcor() > 340:
            self.goto(0, 0)
            self.bounce_x()
            self.ball_speed = 0.1
            return True
        else:
            return False

    def left_paddle_miss(self):
        # Check if the ball misses the left paddle and returns True if it does, otherwise False
        if self.xcor() < -340:
            self.goto(0, 0)
            self.bounce_x()
            self.ball_speed = 0.1
            return True
        else:
            return False
