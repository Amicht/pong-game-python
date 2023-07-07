import time
from turtle import Screen
from ball import Ball
from racket import Racket
from scoreboard import Scoreboard

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
TOP_LIMIT = SCREEN_HEIGHT / 2 - 20
BOTTOM_LIMIT = -1 * SCREEN_HEIGHT / 2 + 20
LEFT_LIMIT = -1 * (SCREEN_WIDTH / 2) + 80
RIGHT_LIMIT = SCREEN_WIDTH / 2 - 80

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)

r_racket = Racket((350, 0), SCREEN_HEIGHT / 2)
l_racket = Racket((-350, 0), SCREEN_HEIGHT / 2)
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(r_racket.up, "Up")
screen.onkey(r_racket.down, "Down")
screen.onkey(l_racket.up, "w")
screen.onkey(l_racket.down, "s")

screen.listen()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Wall collision check:
    if ball.ycor() > TOP_LIMIT or ball.ycor() < BOTTOM_LIMIT:
        ball.bounce_y()

    # Rackets hit check:
    is_hit_left = ball.distance(l_racket) < 40 and ball.xcor() < LEFT_LIMIT
    is_hit_right = ball.distance(r_racket) < 40 and ball.xcor() > RIGHT_LIMIT
    if is_hit_right or is_hit_left:
        ball.bounce_x()

    # On right Racket misses:
    if ball.xcor() > SCREEN_WIDTH / 2 - 20:
        ball.reset_position()
        scoreboard.l_player_point()
    # On left Racket misses:
    if ball.xcor() < -1 * (SCREEN_WIDTH / 2) + 20:
        scoreboard.r_player_point()
        ball.reset_position()


screen.exitonclick()

