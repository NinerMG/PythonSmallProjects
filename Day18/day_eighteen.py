import random
from turtle import Turtle, Screen
from pygame.examples.scrap_clipboard import screen
#Turtle documentation: https://docs.python.org/3/library/turtle.html
#turtle colors: https://trinket.io/docs/colors
import turtle as t
tim = Turtle()
bob = t.Turtle()
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
#bob.shape("turtle")
bob.color("red")

'''
for _ in range(15):
    bob.forward(10)
    bob.penup()
    bob.forward(10)
    bob.pendown()
'''

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

"""
def draw_shape(num_sides):
        for _ in range(num_sides):
            angle = 360 / num_sides
            bob.forward(100)
            bob.right(angle)

for shape_side_n in range(3, 11):
    bob.color(random.choice(colours))
    draw_shape(shape_side_n)
"""


directions = [0,90,180,270]

t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0, 255)
    color = (r,g,b)
    return color

"""
def random_walk(num_steps):
    bob.pensize(15)
    bob.speed("slow")
    for _ in range(1,num_steps):
        bob.color(random_color())
        bob.setheading(random.choice(directions))
        bob.forward(50)

random_walk(100)
"""
#bob.shape("turtle")
bob.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        bob.color(random_color())
        bob.circle(100)
        #current_heading = bob.heading()
        bob.setheading(bob.heading() + size_of_gap)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()