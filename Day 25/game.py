from turtle import Turtle, Screen

class Game(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
    def generate_states(self,x,y,state_name):
        state = Turtle()
        state.hideturtle()
        state.penup()
        state.goto(x,y)
        state.write(state_name)
    def scores(self):
       self.score += 1
    def track(self):
        sc = self.score
        return sc




