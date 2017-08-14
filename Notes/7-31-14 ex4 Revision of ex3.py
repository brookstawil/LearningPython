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

def write_message(x,y,msg):
    setheading(90) #points the turtle to the 90 degree mark
    home_turtle(x,y)

    num_char = len(msg)
    my_heading = (num_char - 1)/2*7
    left(my_heading)

    for ch in msg:
        forward_turtle(300)
        write(ch,align="center",font=("Courier",36,"bold"))
        home_turtle(x,y)
        right(7)
    
def main():
    speed("fastest")
    color("red")

    msg = "I hate you"

    write_message(0,-100,"Howdy! I'm a message")

    color("blue")
    write_message(0,-200,"This is another message!")

    the_message_file = open("secret.txt","r")
    the_message = the_message_file.readline()
    print(the_message)
    the_message_file.close()

    color("purple")
    write(0,-50,the_message)

        
    ht()
    done()
main()
