from turtle import *
from blocks import Blocks
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=800)
screen.listen()
screen.tracer(0)
blocks = Blocks()
paddle = Paddle()

screen.update()

screen.exitonclick()
