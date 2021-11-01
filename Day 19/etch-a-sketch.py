"""Etch-a-Sketch"""
import turtle

tim=turtle.Turtle()
screen=turtle.Screen()

def move_forward():
    """Move Tim forward"""
    tim.forward(20)

def move_backward():
    """Move Tim backward"""
    tim.backward(20)

def move_clockwise():
    """Move Tim clockwise"""
    tim.right(20)

def move_counter_clockwise():
    """Move Tim counter_clockwise"""
    tim.left(20)

def clear_screen():
    """Clear the screen"""
    screen.reset()

screen.listen()
screen.onkeypress(key="w",fun=move_forward)
screen.onkeypress(key="s",fun=move_backward)
screen.onkeypress(key="d",fun=move_clockwise)
screen.onkeypress(key="a",fun=move_counter_clockwise)
screen.onkeypress(key="c",fun=clear_screen)

screen.exitonclick()
