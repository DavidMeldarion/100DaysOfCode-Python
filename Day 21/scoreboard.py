"""Creates scoreboard"""
from turtle import Turtle

ALIGNMENT = "center"

FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    """Initializes the scoreboard"""
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.setposition(0,260)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updates Scoreboard"""
        self.write(f"Score: {self.score}", align=ALIGNMENT,  font=FONT)

    def increase_score(self):
        """Increases the score"""
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        """Alerts the user that the game is over"""
        self.penup()
        self.hideturtle()
        self.setposition(0,0)
        self.color("white")
        self.write("GAME OVER", align=ALIGNMENT,  font=FONT)
