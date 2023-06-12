from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(0.5, 4)
        self.color("#8294C4")
        self.penup()
        self.goto(0, -380)
        self.speed(0)

    def move_left(self):
        x = self.xcor() - 40
        self.goto(x, self.ycor())

    def move_right(self):
        x = self.xcor() + 40
        self.goto(x, self.ycor())
