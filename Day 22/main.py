"""Runs Pong Game"""
from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

scoreboard = Scoreboard()

player_1_score = 0
player_2_score = 0

paddle_r = Paddle((350,0))
paddle_l = Paddle((-350,0))
ball = Ball()

screen.onkeypress(paddle_r.go_up,"Up")
screen.onkeypress(paddle_r.go_down,"Down")

screen.onkeypress(paddle_l.go_up,"w")
screen.onkeypress(paddle_l.go_down,"s")

screen.listen()

GAME_IS_ON = True

while GAME_IS_ON is True:
    time.sleep(ball.move_speed)
    screen.update()
    score = f"{player_1_score} | {player_2_score}"
    scoreboard.update_score(score)
    ball.move()

    #Detect collision with upper and lower walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with right paddle
    if ball.xcor() > 320 and ball.distance(paddle_r) < 50:
        ball.bounce_x()

    #Detect collision with left paddle
    if ball.xcor() < -320 and ball.distance(paddle_l) < 50:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset()
        player_1_score += 1
    if ball.xcor() < -380:
        player_2_score += 1
        ball.reset()

screen.exitonclick()
