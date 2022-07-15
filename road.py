from turtle import Turtle


class Road(Turtle):

    def __init__(self):
        super().__init__()
        self.y_lane = -150

    def create_road(self):
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(300, 200)
        self.pendown()
        self.goto(-300, 200)
        self.penup()
        self.goto(300, -200)
        self.pendown()
        self.goto(-300, -200)

        for lane in range(7):
            self.hideturtle()
            self.color("black")
            self.penup()
            self.goto(275, self.y_lane)
            self.setheading(180)
            for lane_line in range(6):
                self.pendown()
                self.forward(50)
                self.penup()
                self.forward(50)
            self.y_lane += 50
