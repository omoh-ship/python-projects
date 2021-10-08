from turtle import Screen
from paddle import Paddle
from score_board import PlayBoard, Score
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

r_paddle_score = Score((20, 250))
l_paddle_score = Score((-20, 250))


play_board = PlayBoard()
ball = Ball()

screen.listen()
screen.onkey(fun=right_paddle.up, key="Up")
screen.onkey(fun=right_paddle.down, key="Down")
screen.onkey(fun=left_paddle.up, key="w")
screen.onkey(fun=left_paddle.down, key="s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < - 280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.xcor() > 320 and ball.distance(right_paddle) < 50 or ball.xcor() < -320 and ball.distance(left_paddle) < 50:
        ball.bounce_x()

    # Detect paddle miss and add score
    if ball.xcor() > 370:
        ball.refresh()
        l_paddle_score.add_score()
    if ball.xcor() < -370:
        ball.refresh()
        r_paddle_score.add_score()


screen.exitonclick()
