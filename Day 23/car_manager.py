"""Car Managment Class"""
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "blue", "green", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    """Car Manager class"""
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """Create a new car"""
        new_car = Turtle("square")
        y_position=random.randint(-250,250)
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.shapesize(1,2)
        new_car.setpos(300,y_position)
        self.all_cars.append(new_car)

    def move_cars(self):
        """Move the car"""
        for car in self.all_cars:
            car.backward(self.car_speed)
    def level_up(self):
        """Increase car move speed"""
        self.car_speed += MOVE_INCREMENT
