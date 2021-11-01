"""Turtle Race"""
import turtle
import random


def setup_turtle(color, y_cord):
    """Create new turtle instance with inputs of color and starting y cordinates"""
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_cord)
    return new_turtle


screen = turtle.Screen()
screen.setup(width=500, height=400)

IS_GAME_ON = False

USER_BET = screen.textinput(title="Make your bet:", prompt="Which turtle will win the race?"
                            "Enter a color:")

colors = ["red", "green", "yellow", "blue", "purple", "orange"]
y_positions = [25, 75, 125, -25, -75, -125]
all_turtles = []

for i in range(0, 6):
    all_turtles.append(setup_turtle(color=colors[i], y_cord=y_positions[i]))

if USER_BET:
    IS_GAME_ON = True

print (all_turtles)
while IS_GAME_ON is True:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            IS_GAME_ON=False
            winning_color=turtle.pencolor()
            if winning_color is USER_BET:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        else:
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)
    



screen.exitonclick()
