#7/25/14
#Brooks Tawil
#Assignment 5
#This program will run turtle graphics and display a red rectangualar background with a random amount of random shapes!
#I would like to call my abstract painting "Merriment with Randomness"

from turtle import *
import random

#This function gives us a squre, 'i' is the length of the sides
def square(i):
    begin_fill()
    forward(i)
    right(90)
    forward(i)
    right(90)
    forward(i)
    right(90)
    forward(i)
    right(90)
    end_fill()

#This function gives us a rectangualar shape, 'l' is length 'w' is width
def rectangle(l,w):
    begin_fill()
    forward(l)
    right(90)
    forward(w)
    right(90)
    forward(l)
    right(90)
    forward(w)
    right(90)
    end_fill()

#This function gives us an equilateral triangle, 's' is the length of the sides
def triangle(s):
    begin_fill()
    right(120)
    forward(s)
    right(120)
    forward(s)
    right(120)
    forward(s)
    end_fill()

#Gives a red background to the canvas
def background():
    ht()
    color("red")
    pu()
    goto(-300,300)
    pd()
    rectangle(850,750)

#This function assigns one of ten colors in a random order
def rand_color():
    rand_color = random.randint(0,10)

    if(rand_color == 0):
        color("black")
    elif(rand_color == 1):
        color("green")
    elif(rand_color == 2):
        color("blue")
    elif(rand_color == 3):
        color("brown")
    elif(rand_color == 4):
        color("gold")
    elif(rand_color == 5):
        color("pink")
    elif(rand_color == 6):
        color("maroon")
    elif(rand_color == 7):
        color("aqua")
    elif(rand_color == 8):
        color("olive")
    elif(rand_color == 9):
        color("silver")
    else:
        color("purple")

#This function will give us a random amount of random shapes in random locations. SO MUCH RANDOM!!
def rand_shape():

    #Randomly assigns how many shapes will be used
    rand_shape_amt = random.randint(120,160)

    for i in range(rand_shape_amt):

        #Color for this shape in the loop
        rand_color()
        
        #coordinates of the shpae
        x_cord = random.randint(-200,400)
        y_cord = random.randint(-250,200)

        #Sends the cursor to the random location
        pu()
        goto(x_cord,y_cord)

        #Determines the shape and size
        rand_shape = random.randint(0,3)
        pd()
        if rand_shape == 0:
            square_size = random.randint(1,80)
            square(square_size)
        elif rand_shape == 1:
            rect_x = random.randint(1,80) 
            rect_y = random.randint(1,80)
            rectangle(rect_x,rect_y)
        elif rand_shape == 2:
            tri_s = random.randint(1,80)
            triangle(tri_s)
        else:
            begin_fill()
            radius = random.randint(1,80)
            circle(radius)
            end_fill()
    
def main():
    speed("fastest")
    background()
    rand_shape()
    done()

main()
