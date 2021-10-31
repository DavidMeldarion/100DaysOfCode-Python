"""Turtle"""
from turtle import Turtle, Screen, colormode
from random import randint

tim = Turtle()

tim.color("blue")
tim.shape("turtle")
colormode(255)

def shape(dimensions_dict):
    tim.color(randint(0,255),randint(0,255),randint(0,255))
    tim.setheading(0)
    x=dimensions_dict["sides"]
    i=0
    while i < x:
        tim.forward(100)
        tim.right(dimensions_dict["angle"])
        tim.forward(100)
        i+=1

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
x=len(dimensions)
while i < x:
    shape(dimensions[i])
    i+=1
# triangle()
# square()
# pentagon()

screen = Screen()
screen.exitonclick()
