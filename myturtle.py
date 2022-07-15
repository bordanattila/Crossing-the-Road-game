from turtle import Turtle

MOVE_DISTANCE = 25


class Myturtle(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("images/turtle-classic-topview-natural_3.gif")
        self.goto(0, -225)
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def reset_player(self):
        self.goto(0, -225)
