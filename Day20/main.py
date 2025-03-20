#napisanie prostej wersji gry w snake
# na koniec kod powinien być w trzech klasach: Snake, Food, Scoreboard
# Krok 1 stworznie snake body
# Krok 2 jak ruszyć snake
# Krok 3 jak kontrolować snake
# Krok 4 kolizje z jedzeniem - nowe jedzenie, wydłużenie
# Krok 5 liczenie punktów
# Krok 6 wykrycie kolizji ze ścianą
# Krok 7 wykrycie kolizji ze sobą
# dziedziczenie klas
# słowo kluczowe super
# nadpisywanie metod klasy bazowej


from turtle import Screen

from Day20.scoreboard import Scoreboard
from snake import Snake
from food import  Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

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

    #Detect colision with food - distance function
    # creating scoreboard, turtle metoda write oraz metoda clear
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increse_score()

    #Detect colision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake.reset()
        scoreboard.reset()

    #Detect colision with snake tail
    # if head collides with any segment in the tail:
        #trigger game over

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            snake.reset()
            scoreboard.reset()

#Slicing in Python -> co to jest i czemu warto stosowac, przykłady (też te ze stepem)



screen.exitonclick()