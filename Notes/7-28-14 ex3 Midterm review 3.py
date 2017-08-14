#7/28/14
#Midterm Review
#Turtle histogram

from turtle import *

def reset_turtle():
    pu()
    goto(-250,-250)
    pd()

def graph(high):
    begin_fill()
    
    left(90)
    forward(high)
    right(90)
    forward(20)
    right(90)
    forward(high)
    right(90)
    forward(20)
    right(180)
    
    end_fill()

def gotonextnumber():
    pu()
    forward(25)
    pd()

def graphsquare(height):
    print(height)
    graph(height)
    gotonextnumber()
    

def main():
    speed("fastest")
    color("red")

    reset_turtle()

    for x in range (1,21):
        y = x * x
        graphsquare(y)

    ht()
    done()
    
main()
    
