from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self,position):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.goto(position)

    def scores(self):
        self.clear()
        self.write(f"{self.score}", False, align="center", font=("Arial", 18, "normal"))
