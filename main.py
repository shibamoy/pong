from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
from score import Scoreboard

moving_ball = Ball()
line = Turtle()
end_game = Turtle()
screen = Screen()
screen.setup(width=800, height=500)
screen.bgcolor("black")
screen.title("pong game")
screen.tracer(0)
screen.listen()
player_scoreboard = Scoreboard((-40,210))
opponent_scoreboard = Scoreboard((40,210))

player_paddle = Paddle((-380, 0))
opponent_paddle = Paddle((380,0))

screen.onkeypress(player_paddle.move_up, "w")
screen.onkeypress(player_paddle.move_down, "s")

screen.onkeypress(opponent_paddle.move_up, "Up")
screen.onkeypress(opponent_paddle.move_down, "Down")
you = "You"
cpu = "CPU"
def end_of_game(who):
    end_game.penup()
    end_game.color("green")
    end_game.goto(0, 0)
    end_game.write(f"{who} Win! Game Over.", False, align="center", font=("Arial", 18, "normal"))

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

    time.sleep(.01)
    screen.update()
    player_scoreboard.scores()
    opponent_scoreboard.scores()
    moving_ball.move()

    if moving_ball.ycor() > 240 or moving_ball.ycor() < -240:
        moving_ball.bounce_down()
    elif moving_ball.xcor() > 360 and moving_ball.distance(opponent_paddle) < 50 or moving_ball.xcor() < -360 and moving_ball.distance(player_paddle) < 50:
        moving_ball.bounce_wall()

    elif moving_ball.xcor() > 390:
        moving_ball.goto(0,0)
        time.sleep(1)
        player_scoreboard.score += 1
        player_scoreboard.scores()
    elif moving_ball.xcor() < -390:
        moving_ball.goto(0,0)
        time.sleep(1)
        opponent_scoreboard.score += 1
        opponent_scoreboard.scores()
    if opponent_scoreboard.score == 11:
        end_of_game(cpu)
        game = False
    if player_scoreboard.score == 11:
        end_of_game(you)
        game = False


screen.exitonclick()
