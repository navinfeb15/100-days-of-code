from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Set up screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)

# Create objects
ball = Ball()
scoreboard = Scoreboard()
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

# Listen for keyboard inputs
screen.listen()
screen.onkey(fun=right_paddle.go_up, key="Up")
screen.onkey(fun=right_paddle.go_down, key="Down")
screen.onkey(fun=left_paddle.go_up, key="w")
screen.onkey(fun=left_paddle.go_down, key="s")

# Game loop
game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move_ball()
    ball.bounce_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 330:
        ball.bounce_x()
    if ball.distance(left_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    if ball.right_paddle_miss():
        scoreboard.add_score_p1()
    elif ball.left_paddle_miss():
        scoreboard.add_score_p2()

screen.exitonclick()
