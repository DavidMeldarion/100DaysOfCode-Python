"""Defines the ball class"""
from turtle import Turtle

class Ball(Turtle):
    """Defines the Ball class"""
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        """Moves the ball"""
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Reverse direction for y movement"""
        self.y_move = self.y_move * -1

    def bounce_x(self):
        """Reverse direction for x movement"""
        self.x_move = self.x_move * -1
        self.move_speed *= 0.9

    def reset(self):
        """Reset the ball"""
        self.setposition(0,0)
        self.x_move = self.x_move * -1
        self.y_move = self.y_move * -1
        self.move_speed = 0.1
