"""Turtle Crossing Game"""
from random import randint
import time
from turtle import Screen
from scoreboard import Scoreboard
from player import Player
from car_manager import CarManager

#Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing")
screen.tracer(0)

#Class bind to variables
player=Player()
scoreboard = Scoreboard()

screen.onkeypress(player.move, "Up")
screen.listen()

SCORE = 1
LOOP_NUMBER = 0
CARS = []

GAME_IS_ON = True

while GAME_IS_ON is True:
    time.sleep(0.1)
    LOOP_NUMBER += 1
    for item in CARS:
        item.move(SCORE)
        if player.distance(item) < 20:
            GAME_IS_ON = False
    if LOOP_NUMBER % 6 == 0:
        CARS.append(CarManager(randint(-250,250)))
    screen.update()
    scoreboard.update_score(SCORE)
    if player.ycor() >= 280:
        SCORE += 1
        player.player_reset()
scoreboard.game_over()
screen.exitonclick()
