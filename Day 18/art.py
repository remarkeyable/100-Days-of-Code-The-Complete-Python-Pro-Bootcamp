import turtle as pags
import colorgram
import random
from turtle import Screen
pags.colormode(255)
pagong = pags.Turtle()
pagong.shape("circle")
pagong.pensize(1)
pagong.speed("fast")
pagong.penup()
pagong.hideturtle()
colors = colorgram.extract("1168509.jpg", 8)

def stamp(total):
    pagong.setx(-315)
    pagong.sety(-total)
    for i in range(9):
        fclr = colors[random.randint(0, 7)]
        rgb = fclr.rgb
        pagong.color(rgb)
        pagong.stamp()
        pagong.forward(50)
        pagong.stamp()
total = 320
for i in range(10):
    total -= 60
    stamp(total)

screen = Screen()
screen.exitonclick()
