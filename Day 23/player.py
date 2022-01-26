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
        self.go_to_start()

    def move(self):
        """Moves player up by the set MOVE DISTANCE"""
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def is_at_finish_line(self):
        """Checks player position"""
        return self.ycor() > FINISH_LINE_Y
    def go_to_start(self):
        """Resets player to starting position"""
        self.setpos(STARTING_POSITION)
