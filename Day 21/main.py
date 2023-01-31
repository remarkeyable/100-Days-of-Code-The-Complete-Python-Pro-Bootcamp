from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score import Score
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(600, 600)
screen.title("AHAS GAME")
pud = Food()
esn = Snake()
screen.tracer(0)
screen.listen()
screen.onkey(esn.left,"Left")
screen.onkey(esn.right,"Right")
screen.onkey(esn.down,"Down")
screen.onkey(esn.up,"Up")

score = Score()
tes = True
while tes:
    screen.update()
    time.sleep(0.1)
    esn.move()

    if esn.head.distance(pud) < 15 :
        pud.around()
        esn.add_snake()
        score.add_score()

    if esn.head.xcor() > 285 or esn.head.xcor() < -285 or esn.head.ycor() > 250 or esn.head.ycor() < -285:
        score.game_over()
        tes = False

    for body in esn.sneyk[1:]:
        if esn.head.distance(body) < 10:
            score.game_over()
            tes = False

screen.exitonclick()