from turtle import Turtle
import random

COLORS = ["salmon", "pale violet red", "medium aquamarine", "medium purple", "yellow green", "dark cyan"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.set_of_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def produce_cars(self):
        car_chances = random.randint(1, 6)
        if car_chances == 6:
            list_of_y = []
            x = random.randint(300, 350)
            y = random.randint(1, 265)
            y_negative = random.randint(-260, -1)
            list_of_y.append(y)
            list_of_y.append(y_negative)
            yy = random.choice(list_of_y)
            cars = Turtle("square")
            cars.penup()
            cars.shapesize(1, 2)
            cars.setheading(180)
            colors = random.choice(COLORS)
            cars.color(colors)
            cars.goto(x, yy)
            self.set_of_cars.append(cars)

    def forward_cars(self):
        for k in self.set_of_cars:
            k.forward(self.speed)

    def increase(self):
        self.speed += MOVE_INCREMENT






