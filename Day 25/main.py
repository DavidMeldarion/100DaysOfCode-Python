"""States Guessing Game"""
from turtle import Screen, Turtle
from text import Text
import pandas

screen =  Screen()
turtle = Turtle()
screen.title("U.S. States Game")
IMAGE = "blank_states_img.gif"
screen.addshape(IMAGE)
turtle.shape(IMAGE)

states_data = pandas.read_csv("50_states.csv")

state_names = states_data["state"].to_list()

answer_text = Text()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", \
        prompt="Name a state:").title()
    if answer_state == "Exit":
        missed_states = []
        for state in state_names:
            if state not in guessed_states:
                missed_states.append(state)
        pandas.DataFrame(missed_states).to_csv("missed_states.csv")
        break
    if answer_state in state_names and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state = states_data[states_data["state"] == answer_state]
        x_cor = int(state["x"])
        y_cor = int(state["y"])
        answer_text.generate_text(answer_state,x_cor,y_cor)
