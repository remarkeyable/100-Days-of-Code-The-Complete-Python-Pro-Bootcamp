from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.score = 0
        self.goto(150, 230)
        self.write(f"{self.score}", move=False, font=('Arial black', 30, 'normal'))
        self.player2 = Turtle()
        self.player2.color("white")
        self.player2.hideturtle()
        self.player2.penup()
        self.score2 = 0
        self.player2.goto(-150, 230)
        self.player2.write(f"{self.score2}", move=False, font=('Arial black', 30, 'normal'))

    def score_1(self):
        self.clear()
        self.score += 1
        self.write(f"{self.score}", move=False, font=('Arial black', 30, 'normal'))

    def score_2(self):
        self.player2.clear()
        self.score2 += 1
        self.player2.write(f"{self.score2}", move=False, font=('Arial black', 30, 'normal'))




