from turtle import Turtle


class Paddle():
    def __init__(self):
        self.turtle = Turtle()
        self.turtle.shape("square")
        self.turtle.shapesize(1, 8)
        self.turtle.color("#3C486B")
        self.turtle.penup()
        self.turtle.goto(x=0, y=-350)
