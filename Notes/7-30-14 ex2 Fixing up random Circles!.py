#7/30/14
#Circles again
#A revision of the random circle notes from 7/24/14 ex4

from turtle import *
import random

def rand_circle():
    #Creates one random circle
    rand_radius = random.randint(1,50)
    begin_fill()
    circle(rand_radius)
    end_fill()

    color("black")
    write(rand_radius,align="center",font=("Helvetica",10,"bold"))

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

rand_circle_amt = random.randint(10,20)

for i in range(rand_circle_amt):
    main()

