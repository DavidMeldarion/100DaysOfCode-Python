
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.ht()
        self.penup()
        self.goto(0,240)

    def update_score(self, score):
        self.clear()
        self.write(score,False,'center', font=('Courier',40, 'normal'))
