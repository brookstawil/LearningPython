#7/25/14
#Intro to turtle graphics

#Gets all commands from turtle library
from turtle import *

def main():
    #The Turtle starts at 0 degrees

    size = int(input("How big do you want the triangle? "))
    
    #Changes color of pen
    color("papayawhip")

    begin_fill()

    speed("slowest")
    
    #Gives magnitude to the vector
    forward(size)

    #Changes direction of pen, It rotates clockwise
    right(120)

    forward(size)
    right(120)
    forward(size)
    right(120)

    end_fill()

    ht() #Hides the turtle

    done() #When your done with the turtle you MUST end it with the 'done()' function



main()


