from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)
screen.bgcolor("antique white")
string = "Kaninong pagong ka?\nRyn(pink), Rica(lilac), Rose(yellow), Jessa(blue) or Jeco(black) ?".center(24)
bet = screen.textinput("Bet a turtle", f"{string}").lower()


def rand():
    num = random.randint(0, 10)
    return num

ryn = Turtle()
ryn.shape("turtle")
ryn.color("light salmon")
ryn.penup()
ryn.setx(-230)
ryn.sety(-160)


rica = Turtle()
rica.shape("turtle")
rica.color("medium orchid")
rica.penup()
rica.setx(-230)
rica.sety(-80)

jessa = Turtle()
jessa.shape("turtle")
jessa.color("light steel blue")
jessa.penup()
jessa.setx(-230)

rose = Turtle()
rose.shape("turtle")
rose.color("gold")
rose.penup()
rose.setx(-230)
rose.sety(160)

jeco = Turtle()
jeco.shape("turtle")
jeco.penup()
jeco.setx(-230)
jeco.sety(80)


def race():
    status: ""
    weys = True
    while weys:
        ryn.speed("slow")
        ryn.forward(rand())
        if ryn.xcor() > 230:
            status = "ryn"
            weys = False
            return status
        rica.speed("slow")
        rica.forward(rand())
        if rica.xcor() > 230:
            status = "rica"
            weys = False
            return status
        rose.speed("slow")
        rose.forward(rand())
        if rose.xcor() > 230:
            status = "rose"
            weys = False
            return status
        jeco.speed("slow")
        jeco.forward(rand())
        if jeco.xcor() > 230:
            status = "jeco"
            weys = False
            return status
        jessa.speed("slow")
        jessa.forward(rand())
        if jessa.xcor() > 230:
            status = "jessa"
            weys = False
            return status
race()

if race() == bet:
    print("Congrats! You win!")
else:
    print(f"Awwe, you lose. {race()} win.")


screen.exitonclick()