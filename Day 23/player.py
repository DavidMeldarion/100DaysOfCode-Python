"""Player Class"""
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE =  10
FINISH_LINE_Y = 280

class Player(Turtle):
    """Player class"""
    def __init__(self):
        super().__init__()
        self.color("black")
        self.setheading(90)
        self.shape("turtle")
        self.penup()
        self.setpos(0,-280)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def player_reset(self):
        self.setpos(0,-280)
