"""Turtle Class"""
from turtle import Turtle

class Paddle(Turtle):
    """Defines the Paddle class"""
    def __init__(self, position):
        super().__init__()
        self.setheading(90)
        self.shape("square")
        self.shapesize(1,5)
        self.penup()
        self.color("white")
        self.setpos(position)

    def go_up(self):
        """Paddle Move up"""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """Paddle Move Down"""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
        