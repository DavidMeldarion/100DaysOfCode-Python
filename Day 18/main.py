"""Turtle"""
from turtle import Turtle, Screen
import random

tim = Turtle()

tim.color("blue")
tim.shape("turtle")
tim.pensize(1)
tim.speed(0)

screen = Screen()
screen.colormode(255)

def generate_random_color():
    """Make Tim a random color"""
    tim.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))

def move(chosen_direction):
    """Make Tim walk north"""
    generate_random_color()
    tim.seth(chosen_direction)
    tim.forward(100)

directions=[
    90,
    270,
    0,
    180
]

#Creating Spirograph
for i in range(1,360,10):
    generate_random_color()
    tim.circle(100)
    tim.seth(i)

#Creating Random Walk
# for i in range(200):
#     chosen_direction=random.choice(directions)
#     move(chosen_direction)


# def shape(dimensions_dict):
#     """Draws shape based on input dict"""
#     generate_random_color()
#     tim.setheading(0)
#     sides=dimensions_dict["sides"]
#     increment=0
#     while increment < sides:
#         tim.forward(100)
#         tim.right(dimensions_dict["angle"])
#         tim.forward(100)
#         increment+=1

# dimensions=[
#     {"sides": 3,"angle": 120},
#     {"sides":4,"angle": 90},
#     {"sides":5,"angle": 72},
#     {"sides":6,"angle": 60},
#     {"sides":7,"angle": 51.4285714},
#     {"sides":8,"angle": 45},
#     {"sides":9,"angle": 40}
#     ]

# i=0
# LENGTH=len(dimensions)
# while i < LENGTH:
#     shape(dimensions[i])
#     i+=1


screen.exitonclick()
