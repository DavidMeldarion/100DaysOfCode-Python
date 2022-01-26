"""Player Class"""
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE =  10
FINISH_LINE_Y = 280

class Player(Turtle):
    """Player class"""
    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.setpos(STARTING_POSITION)

    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def player_reset(self):
        self.setpos(STARTING_POSITION)
