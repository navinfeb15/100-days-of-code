from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()  # Initialize the parent class (Turtle)
        
        # Set up the turtle's appearance and position
        with open("Day-24\\data.txt") as file_handler:
            self.highscore = int(file_handler.read())
        # data = file_handler.readline()
        # file_handler.close()
        # self.highscore = int(data)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-20, 280)
        self.score = 0
        # self.highscore = int(self.file_handler.readline())
        
        # Set the initial score to 0 and display it
        self.update_scoreboard()

    def add_score(self):
        # Clear the previous score display and increment the score
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
    #     # Move the turtle to the center and display "GAME OVER"
    #     self.goto(0, 20)
    #     self.write("GAME OVER", align="center")

    def update_scoreboard(self):
        self.clear()
        self.write(arg="SCORE : "+str(self.score)+ "  High Score : "+str(self.highscore), align="center")


    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score 
            with open("Day-24\\data.txt", "w") as file_handler:
                file_handler.write(str(self.highscore))
            self.score = 0
        self.update_scoreboard()