from turtle import Turtle


class Blocks():
    def __init__(self):
        super().__init__()
        self.turts = []
        self.turts_restart = []
        self.positions = []
        self.produce_blocks()

    def produce_blocks(self):
        x = -454
        y = 345
        color = "#ff6663"

        for i in range(42):
            x += 115
            self.turtle = Turtle()
            self.turts.append(self.turtle)
            self.turts_restart.append(self.turtle)
            self.turtle.shape("square")
            self.turtle.shapesize(1, 5.4)
            self.turtle.penup()
            self.turtle.goto(x, y)
            self.turtle.color(f"{color}")
            self.turtle.speed(speed=0)
            self.positions.append((self.turtle.xcor(), self.turtle.ycor()))
            if i == 6:
                color = "#feb144"
                x = -454
                y = 315
                y -= 5
            elif i == 13:
                color = "#fdfd97"
                x = -454
                y = 285
                y -= 5
            elif i == 20:
                color = "#9ee09e"
                x = -454
                y = 255
                y -= 5
            elif i == 27:
                color = "#9ec1cf"
                x = -454
                y = 225
                y -= 5
            elif i == 34:
                color = "#cc99c9"
                x = -454
                y = 195
                y -= 5

    def restart(self):
        count = 42
        # Will clear the turtles from turts list
        self.turts.clear()
        # Will copy the turtles from turts restart list to turts list
        self.turts.extend(self.turts_restart)
        # here we iterate the turts to change their colors into original colors
        for i in self.turts:
            count -= 1
            if count < 7:
                i.color("#cc99c9")  # VIOLET
            elif count < 14:
                i.color("#9ec1cf")  # BLUE
            elif count < 21:
                i.color("#9ee09e")  # GREEN
            elif count < 28:
                i.color("#fdfd97")  # YELLOW
            elif count > 42:
                i.color("#feb144")  # ORANGE
