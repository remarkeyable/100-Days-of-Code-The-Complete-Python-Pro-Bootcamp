from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.write(f"Score: {self.score}", False, "center", ('Courier', 15, 'bold'))

    def add_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", False, "center", ('Courier', 15, 'bold'))

    def game_over(self):
        self.clear()
        self.write(f"Amacanna,accla! Your final score:  {self.score}", False, "center", ('Courier', 15, 'bold'))


