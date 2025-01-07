from turtle import Turtle,Screen
from paddle import Paddle
import time

line = Turtle()
screen = Screen()
screen.setup(width=800, height=500)
screen.bgcolor("black")
screen.title("pong game")
screen.tracer(0)
screen.listen()
player_paddle = Paddle((-380, 0))
opponent_paddle = Paddle((380,0))
screen.onkeypress(player_paddle.move_up, "w")
screen.onkeypress(player_paddle.move_down, "s")

screen.onkeypress(opponent_paddle.move_up, "Up")
screen.onkeypress(opponent_paddle.move_down, "Down")

def line_down():
    line.pensize(2)
    line.penup()
    line.color("white")
    line.hideturtle()
    line.goto(0,200)
    line.seth(270)
    for _ in range(10):
        line.pendown()
        line.forward(25)
        line.penup()
        line.forward(25)
line_down()


game = True
while game:

    time.sleep(.1)
    screen.update()
