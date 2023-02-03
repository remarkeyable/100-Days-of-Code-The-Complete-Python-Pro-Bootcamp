import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("pale goldenrod")
player = Player()
score = Scoreboard()
cars = CarManager()
screen.listen()
screen.onkey(player.forward_turtle, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.forward_cars()
    cars.produce_cars()
    for blocks in cars.set_of_cars:
        if blocks.distance(player) < 10:
            score.game_over()
            game_is_on = False
    if player.ycor() > 240:
        score.increase_score()
        cars.increase()
        player.refresh()
screen.exitonclick()



