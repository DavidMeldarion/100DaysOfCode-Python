"""Scoreboard Class"""
from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    """Scoreboard Class"""
    def __init__(self):
        super().__init__()
        self.color("black")
        self.ht()
        self.penup()
        self.goto(0,250)

    def update_score(self, score):
        """Write the score"""
        self.clear()
        self.write(f"Level: {score}",align="center", font = FONT)
 
    def game_over(self):
        """Write Game Over"""
        self.goto(0,0)
        self.write("GAME OVER", align="center", font = FONT)
