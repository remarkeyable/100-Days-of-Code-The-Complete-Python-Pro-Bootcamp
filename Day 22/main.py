from turtle import Turtle, Screen
from paddle import Paddle
from score import Score
from ball import Ball
import time

screen = Screen()
screen.bgcolor("midnight blue")
screen.screensize(600,600)
screen.tracer(0)
screen.listen()
score = Score()
right = Paddle((300, 0))
left = Paddle((-300, 0))
ball = Ball()

screen.onkey(right.w, "Up")
screen.onkey(right.s, "Down")
screen.onkey(left.w, "w")
screen.onkey(left.s, "s")

on = True
while on:
    screen.update()
    time.sleep(ball.ball_speed)
    ball.move()
    if ball.ycor() > 260 or ball.ycor() < -260:
        ball.bounce()
    if ball.distance(right) < 50 and ball.xcor() > 270 or ball.distance(left) < 50 and ball.xcor() < -270:
        ball.bounce2()
    if ball.xcor() > 330:
        score.score_2()
        ball.goto(0,0)
        ball.bounce2()

    if ball.xcor() < -330:
        score.score_1()
        ball.goto(0, 0)
        ball.bounce2()

screen.exitonclick()
