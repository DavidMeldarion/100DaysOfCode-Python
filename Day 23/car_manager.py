"""Car Managment Class"""
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "blue", "green", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    """Car Manager class"""
    def __init__(self, y_position):
        super().__init__()
        self.color(random.choice(COLORS))
        self.penup()
        self.shape('square')
        self.shapesize(1,2)
        self.setpos(300,y_position)

    def move(self,level):
        if level == 1:
            move_distance = STARTING_MOVE_DISTANCE
        else:
            move_distance = STARTING_MOVE_DISTANCE + (MOVE_INCREMENT*level)
        new_x = self.xcor() - move_distance
        self.goto(new_x,self.ycor())
