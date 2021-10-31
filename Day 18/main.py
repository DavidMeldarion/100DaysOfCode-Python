"""Turtle"""
from turtle import Turtle, Screen
from random import randint

tim = Turtle()

tim.color("blue")
tim.shape("turtle")

screen = Screen()
screen.colormode(255)

def shape(dimensions_dict):
    tim.color(randint(0,255),randint(0,255),randint(0,255))
    tim.setheading(0)
    sides=dimensions_dict["sides"]
    increment=0
    while increment < sides:
        tim.forward(100)
        tim.right(dimensions_dict["angle"])
        tim.forward(100)
        increment+=1

dimensions=[
    {"sides": 3,"angle": 120},
    {"sides":4,"angle": 90},
    {"sides":5,"angle": 72},
    {"sides":6,"angle": 60},
    {"sides":7,"angle": 51.4285714},
    {"sides":8,"angle": 45},
    {"sides":9,"angle": 40}
    ]

i=0
length=len(dimensions)
while i < length:
    shape(dimensions[i])
    i+=1


screen.exitonclick()
