#7/30/14
# Printing on the turtle screen

from turtle import *

def main():

    speed("slow")
    #Where is the turtle? Gives us the coordinates
    print( xcor())
    print( ycor())

    pu()
    color("red")
    setx(-100) #This sets the x coordinate of the turtle
    pd()

    begin_fill()
    for times in range(4):
        fd(200)
        left(90)
    end_fill()

    pu()
    sety(-200)
    pd()
    colormode(255) #Now I can set colors to rgb, 0-255

    my_red = 230
    my_green = 230
    my_blue = 0
    color((my_red,my_green,my_blue))
    
    begin_fill()
    for times in range(4):
        fd(200)
        left(90)
    end_fill()

    color("black")

    write("The color chosen was " + str(my_red) + " " + str(my_green) + " " +  str(my_blue),font=("Times",10,"bold"))
    
    ht()
    done()

main()
