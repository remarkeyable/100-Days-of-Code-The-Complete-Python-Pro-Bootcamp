import turtle
import pandas
from game import Game

screen = turtle.Screen()
screen.title("USA Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
game = Game()
on = True
data = pandas.read_csv("50_states.csv")
to_review = (data["state"]).to_list()


while on:
    answer = screen.textinput(title=f" {game.track()}/ 50 States Correct", prompt="Guess the states").title()
    data = pandas.read_csv("50_states.csv")
    x = (data["x"]).to_list()
    y = (data["y"]).to_list()
    states = (data["state"]).to_list()
    if answer in states:
        loc = states.index(answer)
        x = x[loc]
        y = y[loc]
        to_review.remove(answer)
        game.generate_states(x,y,answer)
        game.scores()
    elif answer == "Exit":
        df = pandas.DataFrame(to_review, columns=["States to review"])
        df.to_csv("States_to_review.csv",index=False)
        on = False
    elif game.track() == 50:
        df = pandas.DataFrame(to_review, columns=["States to review"])
        df.to_csv("States_to_review.csv", index=False)
        on = False
screen.exitonclick()

