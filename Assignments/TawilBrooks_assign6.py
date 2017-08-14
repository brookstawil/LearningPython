#7/27/14
#Brooks Tawil
#Assignment 6
#This program will create a unique set of functions to control the turtle

from turtle import *

#This function will set an angle the turtle can use to rotate in the 'L' and 'R' commands
def set_degrees(i):
    return i

#This function will rotate the turtle by a set amount of degrees counter-clockwise, default is 90
def turn_left(i):
    left(i)

#This function will rotate the turtle by a set amount of degrees clockwise, default is 90
def turn_right(i):
    right(i)
    
#This function sets the distance to be used to what the user inputs
distance_default = 1 #If the user never sets the distance this variable will remain true
def set_distance(i):
    return i

#This function will move the turtle forward by the user's set distance
#If 'distance_default' is still tru the turtle will default to a distance of 10
def go_forward(i):
    forward(i)

#This function will change the color of the turtle to red
def set_red():
    color("red")

#This function will change the color of the turtle to blue
def set_blue():
    color("blue")

#This function will change the color of the turtle to green
def set_green():
    color("green")

#This function will change the color of the turtle to black, the default color
def set_black():
    color("black")

#This function will raise the pen
def pen_up():
    pu()

#This function will lower the pen
def pen_down():
    pd()

#This function will end the program
def quit_program():
    done()
    
#The main function will combine all the command functions into a loop
#If the user tells us to stop with the 'Q' command then the loop stops and the program ends
end_loop = 0
def main():
    speed("fastest")
    degree_set = False
    distance_set = False
    end_loop = 0
    while(1 > end_loop):
        user_command = input("What would you like the turtle to do? ")
        user_command = user_command.upper()
        if(user_command == "DIST"):
            user_distance = int(input("What would you like to set the pixel distance to? "))
            distance = set_distance(user_distance)
            distance_set = True
        elif(user_command == "F"):
            if distance_set == True:
                go_forward(distance)
            else:
                forward(10)
        elif(user_command == "DEG"):
            user_degree = int(input("What would you like to set the degree measure to? "))
            degrees = set_degrees(user_degree)
            degree_set = True
        elif(user_command == "L"):
            if degree_set == True:
                turn_left(degrees)
            else:
                turn_left(90)
        elif(user_command == "R"):
            if degree_set == True:
                turn_right(degrees)
            else:
                turn_right(90)
        elif(user_command == "RED"):
            set_red()
        elif(user_command == "BLUE"):
            set_blue()
        elif(user_command == "GREEN"):
            set_green()
        elif(user_command == "BLACK"):
            set_black()
        elif(user_command == "UP"):
            pen_up()
        elif(user_command == "DOWN"):
            pen_down()
        elif(user_command == "Q"):
            break
            quit_program()
        else:
            print("Invalid command, try again")
        
        
main()
print("Enjoy your picture!")







