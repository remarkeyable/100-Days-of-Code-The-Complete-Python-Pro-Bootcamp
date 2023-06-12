from turtle import Turtle

location = [10, -10]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(1, 1)
        self.color("#8294C4")
        self.penup()
        self.x = 10
        self.y = 10
        self.ball_speed = 0.05
        self.goto(0, -330)

    def move(self):
        x = self.xcor() + self.x
        y = self.ycor() + self.y
        self.goto(x, y)

    def bounce(self):
        self.y *= -1

    def bounce_to_paddle(self):
        self.x *= -1
