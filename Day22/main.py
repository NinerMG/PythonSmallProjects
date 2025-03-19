# tworzenie gry pong
# rozbicie problemu na mniejsze kroki
# Krok 1 create the screen (800x600 black, freeze until click on it)
# Krok 2 create and move a paddle (width=20, height=120, x_pos=350, y_pos=0, up and down keys move paddle by 20)
# Krok 3 create another paddle (create class Paddle)
# Krok 4 create the ball and make it move (width=20, height=20, x_pos=0, y_pos=0)
# Krok 5 detect collision with top/down wall and bounce (uwzględnić wielkość piłeczki)
# Krok 6 detect collision with paddle (metoda distant?)
# Krok 7 detect when paddle misses (powinno restartować grę)
# Krok 8 keep score

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #detect r paddle misses
    if ball.xcor() > 390:
        scoreboard.l_point()
        ball.reset_position()

    #detecj l paddle misses
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()

screen.exitonclick()
