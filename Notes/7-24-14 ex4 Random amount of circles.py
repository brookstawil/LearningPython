#7/24/14
# Turtle - random number of circles (15-50)
# Each in a random location on the screen
# In random sizes
# Chosen from five random colors

from turtle import *
import random

def rand_circle():
    #Creates one random circle
    rand_radius = random.randint(1,50)
    begin_fill()
    circle(rand_radius)
    end_fill()

def location():
    #creates a random location
    rand_x = random.randint(-200,200)
    rand_y = random.randint(-200,200)
    pu()
    goto(rand_x,rand_y)
    pd()


def rand_color():
    rand_color_int = random.randint(0,5)   
    if rand_color_int == 0:
        color("blue")
    elif rand_color_int == 1:
        color("green")
    elif rand_color_int == 2:
        color("yellow")
    elif rand_color_int == 3:
        color("red")
    elif rand_color_int == 4:
        color("purple")
    else:
        color("gold")


def main():
    speed("fastest")
    ht()
    rand_color()
    location()
    rand_circle()

rand_circle_amt = random.randint(15,50)

for i in range(rand_circle_amt):
    main()
