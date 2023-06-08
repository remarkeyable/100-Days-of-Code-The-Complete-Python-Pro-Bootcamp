from turtle import Turtle


class Blocks():
    def __init__(self):
        super().__init__()
        self.produce_blocks()

    def produce_blocks(self):
        x = -450
        y = 340
        color = "#ff6663"
        for i in range(42):
            x += 110
            self.turtle = Turtle()
            self.turtle.shape("square")
            self.turtle.shapesize(1, 5)
            self.turtle.penup()
            self.turtle.goto(x, y)
            self.turtle.color(f"{color}")
            self.turtle.speed(speed=0)
            if i == 6:
                color = "#feb144"
                x = -450
                y = 315
                y -= 5
            elif i == 13:
                color = "#fdfd97"
                x = -450
                y = 285
                y -= 5
            elif i == 20:
                color = "#9ee09e"
                x = -450
                y = 255
                y -= 5
            elif i == 27:
                color = "#9ec1cf"
                x = -450
                y = 225
                y -= 5
            elif i == 34:
                color = "#cc99c9"
                x = -450
                y = 195
                y -= 5
