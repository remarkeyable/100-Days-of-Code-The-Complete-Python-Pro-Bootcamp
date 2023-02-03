from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x = 10
        self.y = 10
        self.ball_speed = 0.1

    def move(self):
        x = self.xcor() + self.x
        y = self.ycor() + self.y
        self.goto(x, y)
    def bounce(self):
        self.y *= -1
    def bounce2(self):
        self.x *= -1

