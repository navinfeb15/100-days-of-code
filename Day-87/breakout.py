import turtle
from random import randint

class Breakout:
    def __init__(self):
        # Initialize game variables
        self.life = 3
        self.score = 0
        self.WIDTH, self.HEIGHT = 380, 400
        self.turtle_blocks = []
        self.blocks_area = []

        # Set up the screen
        self.screen = turtle.Screen()
        self.screen.setup(self.WIDTH + 4, self.HEIGHT + 8)
        self.screen.setworldcoordinates(0, 0, self.WIDTH, self.HEIGHT)

        # Set up the main turtle (ball)
        self.main_turtle = turtle.Turtle()
        self.main_turtle.penup()
        self.main_turtle.setheading(randint(20, 160))
        self.main_turtle.setpos(self.WIDTH / 2, 70)
        self.main_turtle.shape('circle')
        self.main_turtle.shapesize(0.5)

        # Set up the paddle
        self.paddle = turtle.Turtle()
        self.paddle.penup()
        self.paddle.setpos(self.WIDTH / 2, 20)
        self.paddle.shape('square')
        self.paddle.shapesize(stretch_len=4)
        self.screen.onkey(lambda: self.paddle.setpos(self.paddle.pos()[0] + 15, self.paddle.pos()[1]), 'Right')
        self.screen.onkey(lambda: self.paddle.setpos(self.paddle.pos()[0] - 15, self.paddle.pos()[1]), 'Left')
        self.screen.listen()

        # Set up labels for lives and score
        self.life_label = turtle.Turtle()
        self.score_label = turtle.Turtle()
        self.life_label.hideturtle()
        self.score_label.hideturtle()
        self.life_label.penup()
        self.score_label.penup()
        self.life_label.setpos(100, self.HEIGHT - 25)
        self.score_label.setpos(self.WIDTH - 100, self.HEIGHT - 25)
        self.score_label.write(f"Score: {self.score}", move=True, align="left")
        self.life_label.write(f"Lives: {self.life}", move=True, align="right")
        self.life_label.color("black")
        self.score_label.color("black")

        # Set up label for game over
        self.game_over_label = turtle.Turtle()
        self.game_over_label.hideturtle()
        self.game_over_label.penup()
        self.game_over_label.setpos(self.WIDTH / 2, self.HEIGHT / 2)
        self.game_over_label.color("black")

    def draw_blocks(self):
        # Draw the blocks on the screen
        self.starty = 330

        for row in range(4):
            self.startx = 40
            while not self.startx + 30 > int(turtle.window_width()) - 40:
                self.blocks_area.append((self.startx, self.starty))
                self.block_turtle = turtle.Turtle()
                self.block_turtle.hideturtle()
                self.block_turtle.penup()
                self.block_turtle.speed(0)
                self.block_turtle.setpos(self.startx, self.starty)

                self.block_turtle.pendown()
                self.block_turtle.setheading(90)
                self.block_turtle.forward(10)
                self.block_turtle.setheading(0)
                self.block_turtle.forward(20)
                self.block_turtle.setheading(270)
                self.block_turtle.forward(10)
                self.block_turtle.setheading(180)
                self.block_turtle.forward(20)
                self.block_turtle.setheading(90)
                self.block_turtle.penup()

                self.turtle_blocks.append(self.block_turtle)
                self.startx += 30

            self.starty -= 20

    def reset_ball(self):
        # Reset the ball position
        self.main_turtle.setpos(self.WIDTH / 2, 70)
        self.main_turtle.setheading(randint(20, 160))

    def wall_bounce(self):
        # Handle ball bouncing off the walls
        ball_pos_x, ball_pos_y = self.main_turtle.pos()

        if ball_pos_x + 20 >= self.WIDTH:  # Right Wall
            heading = self.main_turtle.heading()
            if heading < 90 and heading > 0:
                self.main_turtle.setheading(180 - heading)
            elif heading > 270 or heading <= 359:
                # Coming from top or bottom, reflect heading
                self.main_turtle.setheading(abs(heading - 360) + 180)
            else:
                # Coming straight from left, reverse direction
                self.main_turtle.setheading(180)
        elif ball_pos_x - 20 <= 0:  # Left Wall
            heading = self.main_turtle.heading()
            if heading > 90 and heading < 180:
                # Ball towards top
                self.main_turtle.setheading(180 - heading)
            elif heading > 180 and heading < 270:
                # Ball moving down, reflect around 180
                self.main_turtle.setheading(360 - (heading - 180))
            else:
                # Moving straight right, reverse direction
                self.main_turtle.setheading(heading + 180)

        elif ball_pos_y + 10 >= self.HEIGHT:  # Top wall
            heading = self.main_turtle.heading()
            if heading > 0 and heading < 90:
                self.main_turtle.setheading(360 - heading)
            elif heading > 90 and heading < 180:
                self.main_turtle.setheading(360 - heading)

        elif ball_pos_y - 10 <= 0:  # Bottom wall
            self.life -= 1
            self.reset_ball()
            self.life_label.clear()
            self.life_label.write(f"Lives: {self.life}", move=True, align="right")

    def block_collision(self):
        # Handle ball collision with blocks
        ball_pos_x, ball_pos_y = self.main_turtle.pos()
        ball_radius = 10

        for pos, block_pos in enumerate(self.blocks_area):
            block_x, block_y = block_pos
            block_width = 20
            block_height = 10

            distance_x = abs(ball_pos_x - block_x - block_width / 2)
            distance_y = abs(ball_pos_y - block_y - block_height / 2)

            if distance_x <= block_width / 2 + ball_radius and distance_y <= block_height / 2 + ball_radius:
                self.turtle_blocks[pos].reset()
                self.turtle_blocks.pop(pos)
                self.blocks_area.pop(pos)

                heading = self.main_turtle.heading()
                if 0 < heading < 90 or 90 < heading < 180:
                    self.main_turtle.setheading(360 - heading)
                elif 180 <= heading <= 360:
                    self.main_turtle.setheading(360 - heading)
                self.score += 1
                self.score_label.clear()
                self.score_label.write(f"Score: {self.score}", align="left")
                break

    def paddle_bounce(self):
        # Handle ball bouncing off the paddle
        ball_pos_x, ball_pos_y = self.main_turtle.pos()
        ball_radius = 10
        paddle_x, paddle_y = self.paddle.pos()
        block_width = 80
        block_height = 20
        heading = self.main_turtle.heading()

        distance_x = abs(ball_pos_x - paddle_x - block_width / 2)
        distance_y = abs(ball_pos_y - paddle_y - block_height / 2)

        if distance_x <= block_width / 2 + ball_radius and distance_y <= block_height / 2 + ball_radius:
            self.main_turtle.setheading(360 - heading)

    def play_game(self):
        self.speed = 5
        self.draw_blocks()
        while not self.life < 1:
            self.wall_bounce()
            self.main_turtle.forward(self.speed)
            self.block_collision()
            self.paddle_bounce()
        if self.score == 40:
            self.game_over_label.write(f"YOU WIN", align="center", font=("Arial", 16, "normal"))
        else:
            self.game_over_label.write(f"GAME OVER", align="center", font=("Arial", 16, "normal"))
        turtle.mainloop()


if __name__ == "__main__":
    app = Breakout()
    app.play_game()