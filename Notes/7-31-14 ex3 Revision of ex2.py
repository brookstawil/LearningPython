#7/31/14
#Write a message on the turtle screen one at a time

from turtle import *

def home_turtle(xpos,ypos):
    pu()
    goto(xpos,ypos)
    pd()

def forward_turtle(units):
    pu()
    forward(units)
    pd()

def main():
    speed("fastest")

    home_turtle(0,-150)
    left(90)
    color("red")

    msg = "I hate you "
    num_char = len(msg)
    my_heading = (num_char - 2)/2*5 #half characters to the left
    left(my_heading)
    
    for letter in msg:
        forward_turtle(300)
        write(letter, align="center",font=("Courier",10))
        home_turtle(0,-150)
        right(7)
        
    ht()
    done()
main()
