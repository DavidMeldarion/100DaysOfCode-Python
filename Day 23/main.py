"""Turtle Crossing Game"""
import time
import random
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
car_manager = CarManager()

screen.onkeypress(player.move, "Up")
screen.listen()

SCORE = 1

GAME_IS_ON = True

while GAME_IS_ON is True:
    time.sleep(0.1)
    screen.update()
    random_chance = random.randint(1,6)
    if random_chance == 1:
        car_manager.create_car()
    car_manager.move_cars()
    for car in car_manager.all_cars:
        if car.distance(player) <= 20:
            GAME_IS_ON = False
    scoreboard.update_score(SCORE)
    if player.is_at_finish_line() is True:
        player.go_to_start()
        car_manager.level_up()
        SCORE += 1
scoreboard.game_over()
screen.exitonclick()
