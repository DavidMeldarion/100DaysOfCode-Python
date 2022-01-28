"""Text Writing Class"""
from turtle import Turtle

class Text(Turtle):
    """Text Class"""
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.ht()
    def generate_text(self, answer_state, x_cor, y_cor):
        """Writes text"""
        self.goto(x_cor,y_cor)
        self.write(answer_state)
