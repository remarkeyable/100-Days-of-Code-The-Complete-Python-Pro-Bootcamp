from turtle import Turtle, Screen

pagong = Turtle()
screen = Screen()
screen.listen()



def forward():
    pagong.forward(10)
    click = "w"
    return click
def backward():
    pagong.backward(10)
    click = "s"
    return click
def circ():
    pagong.right(10)
    click = "a"
    return click
def circ2():
    pagong.left(10)
    click = "d"
    return click
def clear():
    pagong.clear()
    click = "c"
    return click


screen.onkey(key = forward(), fun = forward)
screen.onkey(key = backward(), fun = backward)
screen.onkey(key = circ(), fun = circ)
screen.onkey(key = circ2(), fun = circ2)
screen.onkey(key = clear(), fun =clear)
screen.listen()
screen.exitonclick()