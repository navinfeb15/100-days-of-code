import time
from turtle import Turtle


class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.level = 0
    # Initialize the scoreboard attributes
    self.penup()
    self.color("black")
    self.hideturtle()
    self.goto(-230, 280)
    # self.update_scoreboard()
    self.write('LEVEL: ' + str(self.level), align="center",
              font=("Courier", 10, "bold"))

  def update_scoreboard(self):
    # Update the scoreboard display with the current scores
    # Position the turtle at the left score position
    self.level += 1
    self.clear()
    self.write('LEVEL: ' + str(self.level), align="center",
              font=("Courier", 10, "bold"))

  def game_over(self):
    self.clear()
    self.goto(0,0)
    self.write('GAME OVER!! Your Score : ' + str(self.level), align="center",
              font=("Courier", 25, "bold"))