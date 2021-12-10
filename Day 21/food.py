"""Food Class"""
from turtle import Turtle
import random

class Food(Turtle):
    """Creates a food class and inherits from turtle"""
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x,random_y)

    def refresh(self):
        """Send food to new random location"""
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x,random_y)
