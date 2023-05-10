from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()  # Initialize the parent class (Turtle)
        
        # Set up the turtle's appearance and position
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-20, 280)
        
        # Set the initial score to 0 and display it
        self.score = 0
        self.write(arg="SCORE : "+str(self.score), align="center")

    def add_score(self):
        # Clear the previous score display and increment the score
        self.clear()
        self.score += 1
        
        # Display the new score
        self.write(arg="SCORE : "+str(self.score), align="center")

    def game_over(self):
        # Move the turtle to the center and display "GAME OVER"
        self.goto(0, 20)
        self.write("GAME OVER", align="center")