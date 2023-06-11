from turtle import *
from blocks import Blocks
from paddle import Paddle
from ball import Ball
import time
import pygame
from CTkMessagebox import CTkMessagebox
from score import Score

pygame.mixer.init()
blocks_sound = pygame.mixer.Sound("bgs/1.mp3")
wall_paddle_sound = pygame.mixer.Sound("bgs/2.mp3")
game_over = pygame.mixer.Sound("bgs/game_over.mp3")

screen = Screen()
screen.setup(width=790, height=790)
screen.bgcolor("#ECECEC")
screen.tracer(0)
score = Score()
score.the_score()
blocks = Blocks()
ball = Ball()
paddle = Paddle()
screen.listen()
screen.onkey(paddle.move_right, "Up")
screen.onkey(paddle.move_left, "Down")
screen.onkey(paddle.move_left, "Left")
screen.onkey(paddle.move_right, "Right")


def ExitOrPlay():
    msg = CTkMessagebox(title="Game Over", message="Do you still want to play?", icon="question", option_1="Cancel",
                        option_2="No", option_3="Yes")
    response = msg.get()
    if response == "No":
        screen.bye()
    else:
        score.lives += 1
        blocks.restart()

on = True
while on:
    screen.update()
    time.sleep(ball.ball_speed)
    ball.move()
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_to_paddle()
        wall_paddle_sound.play()
    elif ball.ycor() > 380:
        ball.bounce()
        wall_paddle_sound.play()
    elif ball.ycor() < -380:
        score.clear_lives()
        paddle.goto(0, -350)
        ball.goto(0, -310)
        game_over.play()

    elif ball.distance(paddle) < 35:
        ball.bounce()
        wall_paddle_sound.play()
    elif score.lives == 0:
        score.game_over()
        ExitOrPlay()
    for i in blocks.turts:
        if ball.distance(i) < 50:
            ball.bounce()
            score.score += 1
            score.add_score()
            i.color('#DDE6ED')
            blocks.turts.remove(i)
            blocks_sound.play()

screen.exitonclick()
