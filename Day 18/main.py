"""Hirst Painting with Turtle"""
import random
import turtle as t
from colors import color_list

def random_color():
    "Choose a random color from color_list"
    new_color=random.choice(color_list)
    return new_color

tim=t.Turtle()

screen=t.Screen()
screen.colormode(255)

def draw_horizontal():
    """Make Tim draw a horizontal line of dots with a random color and width of 10 dots."""
    for _ in range(1,11):
        color=random_color()
        tim.dot(20,color)
        tim.pd()
        tim.pu()
        tim.forward(50)

y_pos=0
for i in range(1,11):
    tim.setposition(0,y_pos)
    draw_horizontal()
    y_pos+=50

screen.exitonclick()
