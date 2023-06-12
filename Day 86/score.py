from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.text_score = Turtle()
        self.text_score.penup()
        self.text_score.hideturtle()
        self.text_score.color('#526D82')
        self.g_over = Turtle()
        self.g_over.penup()
        self.g_over.hideturtle()
        self.g_over.color('#526D82')
        self.scoree = 0
        self.lives = 3
        self.penup()
        self.color('#526D82')
        self.goto(180, 360)
        self.hideturtle()
        self.write(f"LIVES : x{self.lives} | ", align="center", font=("Courier", 15, "bold"))

    def the_score(self):
        self.text_score.goto(315, 360)
        self.text_score.write(f"SCORE: {self.scoree}", align="center", font=("Courier", 15, "bold"))

    def clear_lives(self):
        self.clear()
        self.lives -= 1
        self.write(f"LIVES : x{self.lives} | ", align="center", font=("Courier", 15, "bold"))

    def add_score(self):
        self.text_score.clear()
        self.text_score.write(f"SCORE: {self.scoree}", align="center", font=("Courier", 15, "bold"))
