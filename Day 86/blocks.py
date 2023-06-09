from turtle import Turtle


class Blocks(Turtle):
    def __init__(self):
        super().__init__()
        color = "#ff6663"
        x = -450
        y = 340
        self.shape("square")
        self.shapesize(1, 5)
        self.penup()
        self.goto(x, y)
        self.color(f"{color}")


    #     self.produce_blocks()
    #
    # def produce_blocks(self):
    #     x = -450
    #     y = 340
    #     color = "#ff6663"
    #     for i in range(42):
    #         x += 110
    #         self.shape("square")
    #         self.shapesize(1, 5)
    #         self.penup()
    #         self.goto(x, y)
    #         self.color(f"{color}")
    #         self.speed(speed=0)
    #         print((self.xcor(),self.ycor()))
    #
    #         if i == 6:
    #             color = "#feb144"
    #             x = -450
    #             y = 315
    #             y -= 5
    #
    #         elif i == 13:
    #             color = "#fdfd97"
    #             x = -450
    #             y = 285
    #             y -= 5
    #         elif i == 20:
    #             color = "#9ee09e"
    #             x = -450
    #             y = 255
    #             y -= 5
    #         elif i == 27:
    #             color = "#9ec1cf"
    #             x = -450
    #             y = 225
    #             y -= 5
    #         elif i == 34:
    #             color = "#cc99c9"
    #             x = -450
    #             y = 195
    #             y -= 5
