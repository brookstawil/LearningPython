#7/24/14
#Seymour Papert's flower

from turtle import *

def side():
    forward(100)
    right(90)

def square():
    begin_fill()
    for i in range (4):
        side()
    end_fill()

def flower():
    for petal in range(20):
        if petal % 4 == 0:
            color("gold")
        elif petal % 4 == 1:
            color("brown")
        elif petal % 4 == 2:
            color("red")
        else:
            color("blue")
        square()
        right(18) #360 degrees divided by 20 petals
        
def main():
    speed("fastest")

    penup()#picks up the pen, pair with the 'pendown()' function 
    goto(0,0) #moves the turtle to a point on the plane
    pendown()

    color("gold")
    flower()

    
main()
