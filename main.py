from turtle import Screen
from cars import Car
from myturtle import Myturtle
from road import Road
from board import Board
import time
import carshapes

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing")
screen.tracer(0)


road = Road()
car = Car()
board = Board()
player = Myturtle()

screen.listen()
screen.onkey(player.go_up, "Up")

road.create_road()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    car.create_car()
    car.move_car()

    # Detecting collision with car
    for hit_car in car.list_of_cars:
        if hit_car.distance(player) < 20:
            game_is_on = False
            board.game_over()

    # Finishing level
    if player.ycor() > 200:
        board.next_level()
        player.reset_player()
        car.speed_up_car()

    # Removing cars that passed the screen
    for car_passed in car.list_of_cars:
        if car_passed.xcor() < -380:
            car.list_of_cars.remove(car_passed)

screen.exitonclick()
