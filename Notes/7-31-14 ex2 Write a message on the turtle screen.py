#7/31/14
#Write a message on the turtle screen one at a time

from turtle import *

def home_turtle(xpos,ypos):
    pu()
    goto(xpos,ypos)
    pd()

def forward_turtle():
    pu()
    setx(xcor() + 10)
    pd()

def main():
    speed("fastest")

    home_turtle(-200,200)

    msg1 = "Error, please try again.\n"
    msg2 = "Open the pod bay doors Hal.\n"
    msg3 = "I'm sorry Dave I can't let you do that.\n"

    for letter in msg1:
        write(letter, align="center",font=("Courier",12))
        forward_turtle()

    home_turtle(-200,185)
    for letter in msg2:
        color("red")
        write(letter, align="center",font=("Courier",12))
        forward_turtle()

    home_turtle(-200,170)
    for letter in msg3:
        color("black")
        write(letter, align="center",font=("Courier",12))
        forward_turtle()
    ht()
    done()
main()
