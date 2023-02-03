from turtle import Turtle
FONT = ("Calibri", 15, "normal")
FONT2 = ("Calibri", 15, "normal")

class Scoreboard(Turtle):
   def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.color("olive drab")
        self.goto(-290, 260)
        self.hideturtle()
        self.score()

   def score(self):
       self.write(f"Level: {self.level}", font=FONT)

   def game_over(self):
       self.clear()
       self.write(f"Amacana, accla. Your final score: {self.level}", font=FONT2)



   def increase_score(self):
       self.level += 1
       self.clear()
       self.score()







