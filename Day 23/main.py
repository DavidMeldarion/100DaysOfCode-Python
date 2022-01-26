"""Turtle Crossing Game"""
import time
from turtle import Screen
from scoreboard import Scoreboard
from player import Player

#Class bind to variables
player=Player()
scoreboard = Scoreboard()

#Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing")
screen.tracer(0)

screen.onkey(print("move"), "Up")
screen.listen()

GAME_IS_ON = True

while GAME_IS_ON is True:
    time.sleep(0.1)
    screen.update()
    SCORE = "0"
    # scoreboard.update_score(SCORE)
    # if player.ycor() == 280:
    #     SCORE += 1
    #     player.reset()

screen.exitonclick()
