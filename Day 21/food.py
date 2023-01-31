from turtle import Turtle
from snake import Snake
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("white")
        self.speed("fastest")
        self.around()

    def around(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 250)
        self.goto(x,y)


