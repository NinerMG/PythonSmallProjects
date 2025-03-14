from turtle import Turtle, Screen
from pygame.examples.scrap_clipboard import screen
#Turtle documentation: https://docs.python.org/3/library/turtle.html
#turtle colors: https://trinket.io/docs/colors

tim = Turtle()
bob = Turtle()
'''
tim.shape("turtle")
tim.color('red')
tim.forward(100)
tim.right(90)
tim.forward(100)
tim.right(90)
tim.forward(100)
tim.right(90)
tim.forward(100)
'''

'''
tim.color("green")
for _ in range(4):
    tim.forward(200)
    tim.left(90)
'''
bob.shape("arrow")
bob.color("red")

for _ in range(15):
    bob.forward(10)
    bob.penup()
    bob.forward(10)
    bob.pendown()













screen = Screen()
screen.exitonclick()