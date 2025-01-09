from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.y = 10
        self.x =10


    def move(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x,new_y)
        
    def bounce_down(self):
        self.y *= -1
        
    def bounce_wall(self):
        self.x *= -1
