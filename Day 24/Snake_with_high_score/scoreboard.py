from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score =  self.store_score()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()
        self.hs_update()

    def update_scoreboard(self):
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)


    def reset(self):
        self.clear()
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()


    def hs_update(self):
        with open("score.txt", mode= "w") as data_base:
            data_base.write(str(self.high_score))

    def store_score(self):
        with open("score.txt", mode="r") as wid:
            self.hs = wid.read()
            self.high_score = int(self.hs)
            return self.high_score






