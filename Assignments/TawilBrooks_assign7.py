#8/3/14
#Brooks Tawil
#Assignment 7: This program will run the functions used to make a fourteen point display of characters
#This will read in the disk file 'TawilBrooks_asssign7_library.py'
#Note: Make sure to put this file in the same directory as 'TawilBrooks_asssign7_library.py'

from turtle import *

#Writes a text file that contains the width that will be used to make the characters
Tawil_width = open('TawilBrooksWidth.txt','w')

Tawil_width.write('100')

Tawil_width.close()

#Reads a text file that contains the width
Tawil_width = open('TawilBrooksWidth.txt','r')

width = Tawil_width.read()
width = int(width)

Tawil_width.close()

speed('fastest')

user_word = input("Give me a phrase to write. ")
user_word = user_word.upper()

#These cordinates are used after every brush stroke, they will be changed later to form ne letters
home_x = -200
home_y = 150

#########This is the section of functions that contains the different kinds of rectangles used#########
def border(width):
    color('black')
    turtle_home(home_x,home_y)
    pd()
    forward(width)
    left(90)
    forward(width)
    left(90)
    forward(width)
    left(90)
    forward(width)
    left(90)

#Shape used to make the lines vertically
def rectangle_tall(width):
    color('red')
    begin_fill()
    forward(width * .2)
    left(90)
    forward(width * .4)
    left(90)
    forward(width * .2)
    left(90)
    forward(width * .4)
    left(90)
    end_fill()

#Shape used to make the lines horizantally
def rectangle_wide(width):
    color('red')
    begin_fill()
    forward(width * .5)
    left(90)
    forward(width * .2)
    left(90)
    forward(width * .5)
    left(90)
    forward(width * .2)
    left(90)
    end_fill()

#Shape used to make small lines horizantally
def small_rectangle_wide(width):
    color('red')
    begin_fill()
    forward(width * .25)
    left(90)
    forward(width * .1)
    left(90)
    forward(width * .25)
    left(90)
    forward(width * .1)
    left(90)
    end_fill()

#Shape used to make the small lines vertically
def small_rectangle_tall(width):
    color('red')
    begin_fill()
    forward(width * .1)
    left(90)
    forward(width * .33)
    left(90)
    forward(width * .1)
    left(90)
    forward(width * .33)
    left(90)
    end_fill()

def small_diagonal_rectangle(width):
    color('red')
    begin_fill()
    forward(width * .1)
    left(90)
    forward(width * .4)
    left(90)
    forward(width * .1)
    left(90)
    forward(width * .4)
    left(90)
    end_fill()

def small_diagonal_rectangle1(width):
    color('red')
    begin_fill()
    forward(width * .1)
    right(90)
    forward(width * .4)
    right(90)
    forward(width * .1)
    right(90)
    forward(width * .4)
    right(90)
    end_fill()

#########This section contains the functions for the fourteen individual segments#########
    
#Resets the turtle for next stroke
def turtle_home(home_x,home_y):
    pu()
    goto(home_x,home_y)
    setheading(0)

#Makes a rectangle in the bottom left of the display
def bottom_left_stroke():
    turtle_home(home_x,home_y)
    rectangle_tall(width)

#Makes a rectangle in the top right of the display
def top_left_stroke():
    turtle_home(home_x,home_y)
    goto((home_x),(home_y + width * .45))
    pd()
    rectangle_tall(width)

#Makes the top stroke of the character
def top_stroke(width):
    turtle_home(home_x,home_y)
    goto((home_x + width * .25),(home_y + width *.85))
    pd()
    rectangle_wide(width)

#Makes the top right stroke
def top_right_stroke(width):
    turtle_home(home_x,home_y)
    goto((home_x + width * .8),(home_y + width * .45)) #When the width of the character is used change this!
    pd()
    rectangle_tall(width)

#Makes the bottom rigth stroke
def bottom_right_stroke(width):
    turtle_home(home_x,home_y)
    goto((home_x + width * .8),(home_y))
    pd()
    rectangle_tall(width)

#Makes the bottom stroke
def bottom_stroke(width):
    turtle_home(home_x,home_y)
    goto((home_x + width * .25),(home_y - width * .2))
    pd()
    rectangle_wide(width)

#makes a small stroke in the middle on the left
def left_middle_stroke(width):
    turtle_home(home_x,home_y)
    goto((home_x + width * .22),(home_y + width * .375))
    pd()
    small_rectangle_wide(width)

#makes a small stroke in the middle on the right
def right_middle_stroke(width):
    turtle_home(home_x,home_y)
    goto((home_x + width * .52),(home_y + width * .375))
    pd()
    small_rectangle_wide(width)

#Makes a vertical line in the top middle
def top_inside_stroke(width):
    turtle_home(home_x,home_y)
    goto((home_x + width * .44),(home_y + width * .5))
    pd()
    small_rectangle_tall(width)

#Makes a vertical line in the bottom middle
def bottom_inside_stroke(width):
    turtle_home(home_x,home_y)
    goto((home_x + width * .44),(home_y + width * .03))
    pd()
    small_rectangle_tall(width)
    
#Makes a bottom left diagonal line
def bottom_left_diagonal(width):
    turtle_home(home_x,home_y)
    pu()
    goto(home_x + (width * .2),home_y + (width * .05))
    pd()
    right(30)
    small_diagonal_rectangle(width)

#Makes a bottom right diagonal line
def bottom_right_diagonal(width):
    turtle_home(home_x,home_y)
    pu()
    goto(home_x + (width * .71),home_y + (width * .005))
    pd()
    left(30)
    small_diagonal_rectangle(width)

#Makes a top left diagonal line
def top_left_diagonal(width):
    turtle_home(home_x,home_y)
    pu()
    goto(home_x + (width * .2),home_y + (width * .79))
    pd()
    left(30)
    small_diagonal_rectangle1(width)

#Makes a top right diagonal
def top_right_diagonal(width):
    turtle_home(home_x,home_y)
    pu()
    goto(home_x + (width * .795),home_y + (width * .79))
    pd()
    left(150)
    small_diagonal_rectangle(width)

#########This section coontains all of the combinations of the various segments to form long strokes#########

#Combines the two small left strokes into one large stroke
def left_stroke():
    bottom_left_stroke()
    top_left_stroke()

#Combines the two small right strokes to make a single right stroke
def right_stroke():
    top_right_stroke(width)
    bottom_right_stroke(width)

#Makes a large middle horizantal stroke
def horizontal_middle_stroke():
    left_middle_stroke(width)
    right_middle_stroke(width)

#Combines the two small middle strokes into one large vertical stroke
def vertical_middle_stroke():
    top_inside_stroke(width)
    bottom_inside_stroke(width)

#Combines two diagonals to form a forward slash like '\'
def forward_slash():
    top_left_diagonal(width)
    bottom_right_diagonal(width)

#Combines two diagonals to form a backward slash like '/'
def backward_slash():
    top_right_diagonal(width)
    bottom_left_diagonal(width)

#########This section contains the new_letter function and the new_line function
def new_letter():
    global home_x
    home_x += (width + 15)

def new_line():
    global home_y
    global home_x
    home_y -= width + 35
    home_x = -200
    
#########This section contains the various full characters that can be made
#A
def letter_A():
    top_stroke(width)
    left_stroke()
    horizontal_middle_stroke()
    right_stroke()

#B
def letter_B():
    top_stroke(width)
    vertical_middle_stroke()
    right_middle_stroke(width)
    right_stroke()
    bottom_stroke(width)

#C
def letter_C():
    top_stroke(width)
    left_stroke()
    bottom_stroke(width)

#D
def letter_D():
    top_stroke(width)
    vertical_middle_stroke()
    right_stroke()
    bottom_stroke(width)

#E
def letter_E():
    left_stroke()
    bottom_stroke(width)
    top_stroke(width)
    left_middle_stroke(width)

#F
def letter_F():
    left_stroke()
    top_stroke(width)
    left_middle_stroke(width)

#G
def letter_G():
    left_stroke()
    top_stroke(width)
    right_middle_stroke(width)
    bottom_stroke(width)

#H
def letter_H():
    left_stroke()
    right_stroke()    
    horizontal_middle_stroke()

#I
def letter_I():
    bottom_stroke(width)
    top_stroke(width)
    vertical_middle_stroke()

#J
def letter_J ():
    bottom_stroke(width)
    right_stroke()
    bottom_left_stroke()

#K
def letter_K():
    left_stroke()
    left_middle_stroke(width)
    bottom_right_diagonal(width)
    top_right_diagonal(width)

#L
def letter_L():
    left_stroke()
    bottom_stroke(width)

#M
def letter_M():
    left_stroke()
    top_left_diagonal(width)
    top_right_diagonal(width)
    right_stroke()

#N
def letter_N():
    left_stroke()
    forward_slash()
    right_stroke()

#O
def letter_O():
    top_stroke(width)
    bottom_stroke(width)
    left_stroke()
    right_stroke()

#P
def letter_P():
    left_stroke()
    top_stroke(width)
    horizontal_middle_stroke()
    top_right_stroke(width)

#Q
def letter_Q():
    top_stroke(width)
    bottom_stroke(width)
    left_stroke()
    right_stroke()
    bottom_right_diagonal(width)

#R
def letter_R():
    top_stroke(width)
    left_stroke()
    horizontal_middle_stroke()
    top_right_stroke(width)
    bottom_right_diagonal(width)

#S
def letter_S():
    top_stroke(width)
    bottom_stroke(width)
    top_left_diagonal(width)
    right_middle_stroke(width)
    bottom_right_stroke(width)

#T
def letter_T():
    top_stroke(width)
    vertical_middle_stroke()

#U
def letter_U():
    left_stroke()
    right_stroke()
    bottom_stroke(width)

#V
def letter_V():
    left_stroke()
    backward_slash()

#W
def letter_W():
    left_stroke()
    bottom_left_diagonal(width)
    bottom_right_diagonal(width)
    right_stroke()

#X
def letter_X():
    forward_slash()
    backward_slash()

#Y
def letter_Y():
    top_left_diagonal(width)
    top_right_diagonal(width)
    bottom_inside_stroke(width)

#Z
def letter_Z():
    top_stroke(width)
    backward_slash()
    bottom_stroke(width)

#########This section contains the functions used to write numbers#########

#0
def number_0():
    top_stroke(width)
    left_stroke()
    right_stroke()
    bottom_stroke(width)

#1
def number_1():
    right_stroke()
    top_right_diagonal(width)

#2
def number_2():
    top_stroke(width)
    top_right_stroke(width)
    horizontal_middle_stroke()
    bottom_left_stroke()
    bottom_stroke(width)

#3
def number_3():
    top_stroke(width)
    right_stroke()
    horizontal_middle_stroke()
    bottom_stroke(width)    
    
#4
def number_4():
    horizontal_middle_stroke()
    top_left_stroke()
    right_stroke()

#5
def number_5():
    top_stroke(width)
    top_left_stroke()
    horizontal_middle_stroke()
    bottom_right_stroke(width)
    bottom_stroke(width)

#6
def number_6():
    top_stroke(width)
    left_stroke()
    horizontal_middle_stroke()
    bottom_right_stroke(width)
    bottom_stroke(width)

#7
def number_7():
    top_stroke(width)
    backward_slash()

#8
def number_8():
    top_stroke(width)
    left_stroke()
    horizontal_middle_stroke()
    right_stroke()    
    bottom_stroke(width)

#9
def number_9():
    top_stroke(width)
    top_left_stroke()
    horizontal_middle_stroke()
    right_stroke()

for letter in user_word:
    if letter == 'A':
        letter_A()
        new_letter()
    elif letter == 'B':
        letter_B()
        new_letter()
    elif letter == 'C':
        letter_C()
        new_letter()
    elif letter == 'D':
        letter_D()
        new_letter()
    elif letter == 'E':
        letter_E()
        new_letter()
    elif letter == 'F':
        letter_F()
        new_letter()
    elif letter == 'G':
        letter_G()
        new_letter()
    elif letter == 'H':
        letter_H()
        new_letter()
    elif letter == 'I':
        letter_I()
        new_letter()
    elif letter == 'J':
        letter_J()
        new_letter()
    elif letter == 'K':
        letter_K()
        new_letter()
    elif letter == 'L':
        letter_L()
        new_letter()
    elif letter == 'M':
        letter_M()
        new_letter()
    elif letter == 'N':
        letter_N()
        new_letter()
    elif letter == 'O':
        letter_O()
        new_letter()
    elif letter == 'P':
        letter_P()
        new_letter()
    elif letter == 'Q':
        letter_Q()
        new_letter()
    elif letter == 'R':
        letter_R()
        new_letter()
    elif letter == 'S':
        letter_S()
        new_letter()
    elif letter == 'T':
        letter_T()
        new_letter()
    elif letter == 'U':
        letter_U()
        new_letter()
    elif letter == 'V':
        letter_V()
        new_letter()
    elif letter == 'W':
        letter_W()
        new_letter()
    elif letter == 'X':
        letter_X()
        new_letter()
    elif letter == 'Y':
        letter_Y()
        new_letter()
    elif letter == 'Z':
        letter_Z()
        new_letter()
    elif letter == '1':
        number_1()
        new_letter()
    elif letter == '2':
        number_2()
        new_letter()
    elif letter == '3':
        number_3()
        new_letter()
    elif letter == '4':
        number_4()
        new_letter()
    elif letter == '5':
        number_5()
        new_letter()
    elif letter == '6':
        number_6()
        new_letter()
    elif letter == '7':
        number_7()
        new_letter()
    elif letter == '8':
        number_8()
        new_letter()
    elif letter == '9':
        number_9()
        new_letter()
    elif letter == '0':
        number_0()
        new_letter()
    elif letter == ' ':
        new_line()
    else:
        print(letter,"cannot be printed. This program only prints Capital letters, numbers and spaces")

ht()
done()
        
