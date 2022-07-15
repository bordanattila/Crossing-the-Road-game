from turtle import Turtle
import random

CAR_TYPES = ["images/right_police.gif", "images/right_taxi.gif", "images/red_right.gif", "images/grey_right.gif",
             "images/blue_right.gif"]
COLOURS = ["red", "blue", "yellow", "green", "orange", "purple"]
MOVE_INCREMENT = 5
LANES = [175, 125, 75, 25, -25, -75, -125, -175]


class Car:

    def __init__(self):
        self.list_of_cars = []
        self.MOVE_DISTANCE = 5

    def create_car(self):
        car_type = random.choice(CAR_TYPES)
        car_generation = random.randint(1, 6)
        if car_generation == 1:
            my_car = Turtle()
            my_car.penup()
            my_car.shape(car_type)
            if my_car.xcor() == 300:
                my_car.goto(340)
            else:
                my_car.goto(300, random.choice(LANES))
            my_car.color(random.choice(COLOURS))
            self.list_of_cars.append(my_car)

    def move_car(self):
        for move in self.list_of_cars:
            move.backward(self.MOVE_DISTANCE)

    def speed_up_car(self):
        self.MOVE_DISTANCE += MOVE_INCREMENT
        self.move_car()
