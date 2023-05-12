from turtle import Turtle, Screen

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        # Initialize the scoreboard attributes
        self.penup()
        self.color("white")
        self.hideturtle()
        self.PLAYER1 = 0
        self.PLAYER2 = 0
        self.update_scoreboard()

    def add_score_p1(self):
        # Increase player 1's score and update the scoreboard
        self.clear()
        self.PLAYER1 += 1
        self.update_scoreboard()

    def add_score_p2(self):
        # Increase player 2's score and update the scoreboard
        self.clear()
        self.PLAYER2 += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        # Update the scoreboard display with the current scores
        self.goto(-50, 260)  # Position the turtle at the left score position
        self.write(arg=self.PLAYER1, align="center", font=("Courier", 20, "normal"))  # Write player 1's score
        self.goto(50, 260)  # Position the turtle at the right score position
        self.write(arg=self.PLAYER2, align="center", font=("Courier", 20, "normal"))  # Write player 2's score
