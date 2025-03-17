#napisanie prostej wersji gry w snake
# na koniec kod powinien być w trzech klasach: Snake, Food, Scoreboard
# Krok 1 stworznie snake body
# Krok 2 jak ruszyć snake
# Krok 3 jak kontrolować snake
# Krok 4 kolizje z jedzeniem - nowe jedzenie, wydłużenie
# Krok 5 liczenie punktów
# Krok 6 wykrycie kolizji ze ścianą
# Krok 7 wykrycie kolizji ze sobą


from turtle import Turtle, Screen
from snake import Snake
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()


screen.exitonclick()