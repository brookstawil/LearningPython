#7/24/14
#Circles!

from turtle import *

def main():

    speed("fastest")

    size = 110 #size of first circle

    num_circles = 10

    for i in range(num_circles):
        if i % 4 == 0:
            color("gold")
        elif i % 4 == 1:
            color("brown")
        elif i % 4 == 2:
            color("red")
        else:
            color("blue")

        begin_fill()
        circle(size)
        end_fill()

        size -= 10


    ht()
    done()


main()
