from turtle import *
from blocks import Blocks
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("#F8F6F4")
screen.tracer(0)
blocks = Blocks()
ball = Ball()
right = Paddle((0, -350))
screen.listen()
screen.onkey(right.move_right, "Up")
screen.onkey(right.move_left, "Down")
screen.onkey(right.move_left, "Left")
screen.onkey(right.move_right, "Right")

# x = -450
# y = 340
# color = "#ff6663"
# for i in range(42):
#     x += 110
#     # blocks.shape("square")
#     # blocks.shapesize(1, 5)
#     # blocks.penup()
#     # blocks.goto(x, y)
#     # blocks.color(f"{color}")
#     # blocks.speed(speed=0)
#
#     if i == 6:
#         color = "#feb144"
#         x = -450
#         y = 315
#         y -= 5

on = True
while on:
    screen.update()
    time.sleep(ball.ball_speed)
    ball.move()
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_to_paddle()
    # if ball.turtle.distance(blocks.turtle) < 20:
    #     print("hello")
    #     ball.turtle.bounce_to_paddle()

    # if (blocks.turtle.xcor(),b.turtle.ycor()) > blocks.turtle.xcor():
    #     blocks.turtle.color('white')
    #     print("nya")
    if ball.distance(blocks) < 50:
        print('hello')

screen.exitonclick()
