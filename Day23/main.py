#Budowa gry crossing roads
#żółw chce przejść przez ulice


import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player_one = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player_one.go_up, "Up")
screen.onkey(player_one.go_down, "Down")
screen.onkey(player_one.go_left, "Left")
screen.onkey(player_one.go_right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()

    #detect collison with car
    for car in car_manager.all_cars:
       if  car.distance(player_one) < 20:
        game_is_on = False
        scoreboard.game_over()

    if player_one.is_at_finish_line():
        player_one.go_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()