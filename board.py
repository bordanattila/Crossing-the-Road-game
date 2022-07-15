from turtle import Turtle
ALIGNMENT = "left"
FONT = ("Courier", 22, "normal")


class Board(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-250, 250)
        self.color("black")
        self.level = 1
        self.update_board()

    def update_board(self):
        self.clear()
        self.write(f"Level: {self.level}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align="center", font=("Courier", 24, "bold"))

    def next_level(self):
        self.level += 1
        self.update_board()
