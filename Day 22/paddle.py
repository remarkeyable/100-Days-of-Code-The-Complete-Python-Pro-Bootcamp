from turtle import Turtle
LOCATION = [(-300,0), (300,0)]

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 0.3)
        self.penup()
        self.goto(position)
        self.pos()

    def pos(self):
        x = 0
        y = 287
        for i in range(18):
            y -= 30
            design = Turtle("square")
            design.color("white")
            design.penup()
            design.shapesize(0.8, 0.2, 1)
            design.goto(x, y)
    def w(self):
        y = self.ycor() + 30
        self.goto(self.xcor(), y)
    def s(self):
        y = self.ycor() - 30
        self.goto(self.xcor(), y)








    





