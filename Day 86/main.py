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
screen.title("Breakout Game")
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
    msg = CTkMessagebox(title="Game Over", message="GAME OVER ! \n\nDo you still want to play?", icon="question",
                        option_1="No", option_2="Yes")
    response = msg.get()
    if response == "No":
        screen.bye()
    else:
        blocks.restart()
        print(blocks.turts)
        print(blocks.turts_restart)
        score.lives += 3
        score.scoree = 0
        score.clear()
        score.text_score.clear()
        score.write(f"LIVES : x{score.lives} | ", align="center", font=("Courier", 15, "bold"))
        score.text_score.write(f"SCORE: {score.scoree}", align="center", font=("Courier", 15, "bold"))


on = True
while on:
    screen.update()
    time.sleep(ball.ball_speed)
    ball.move()
    if ball.xcor() > 385 or ball.xcor() < -385:
        ball.bounce_to_paddle()
        wall_paddle_sound.play()
    elif ball.ycor() > 385:
        ball.bounce()
        wall_paddle_sound.play()
    elif ball.ycor() < -380:
        score.clear_lives()
        paddle.goto(0, -380)
        ball.goto(0, -350)
        game_over.play()

    elif ball.distance(paddle) < 30:
        ball.bounce()
        wall_paddle_sound.play()
    elif score.lives == 0:
        ExitOrPlay()
    for i in blocks.turts:
        if ball.distance(i) < 50:
            ball.bounce()
            score.scoree += 1
            score.add_score()
            i.color('#DDE6ED')
            blocks.turts.remove(i)
            blocks_sound.play()

screen.exitonclick()
