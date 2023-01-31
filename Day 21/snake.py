from turtle import Turtle
NEW = [(0, 0), (-20, 0), (-40, 0)]
MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:

    def __init__(self):
        self.sneyk = []
        self.first()
        self.head = self.sneyk[0]


    def first(self):
        for i in NEW:
            turts = Turtle("square")
            turts.color('white')
            turts.penup()
            turts.goto(i)
            self.sneyk.append(turts)

    def move(self):
        for new in range(len(self.sneyk) - 1, 0, -1):
            nx = self.sneyk[new - 1].xcor()
            ny = self.sneyk[new - 1].ycor()
            self.sneyk[new].goto(nx, ny)
        self.sneyk[0].forward(MOVE)


    def left(self):
        if self.head.heading() != RIGHT:
            self.sneyk[0].setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.sneyk[0].setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.sneyk[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.sneyk[0].setheading(DOWN)

    def add_snake(self):
        length = len(self.sneyk)
        towts = Turtle("square")
        towts.color('white')
        towts.penup()
        nx = self.sneyk[length -1].xcor()
        ny = self.sneyk[length -1 ].ycor()
        towts.goto(nx, ny)
        self.sneyk.append(towts)