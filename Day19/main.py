from turtle import Turtle, Screen

#tuples, turtle graphics, event listeners, state and multiple instances
# przekazywanie funkcji do paramterów funkcji
#funkcja wyższego rzędu


tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def clear_board():
     tim.clear()
     tim.penup()
     tim.home()
     tim.pendown()

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_right, "a")
screen.onkey(turn_left, "d")
screen.onkey(clear_board, "c")
screen.exitonclick()