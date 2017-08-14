#7/31/14
#Library of different shapes to be used in turtle
#ALL SHAPES START FROM THE BOTTOM LEFT OF A DEFINED SHAPE

from turtle import *

#Use this to draw a square
def square(units):
    forward(units)
    left(90)
    forward(units)
    left(90)
    forward(units)
    left(90)
    forward(units)
    left(90)

#Use this to draw a rectangle
def rectangle(width,height):
    forward(width)
    left(90)
    forward(height)
    left(90)
    forward(width)
    left(90)
    forward(height)
    left(90)

#Use this to draw an equilateral triangle triangle
def triangle(units):
    forward(units)
    left(120)
    forward(units)
    left(120)
    forward(units)
    left(120)
    

#Use this to draw a triangle with interchangable angles and sides
#(angleX,angleY,angleZ then the sides sideX,sideY,sideZ)
def custom_triangle(ang_x,ang_y,ang_z,side_x,side_y,side_z):
    correct_triangle = False

    #Finds the largest angle
    if (ang_x > ang_y and ang_x > ang_z):
        largest_angle = ang_x
    elif(ang_y > ang_x and ang_y > ang_z):
        largest_angle = ang_y
    else:
        largest_angle = ang_z

    #Finds the largest side
    if (side_x > side_y and side_x > side_z):
        largest_side = side_x
    elif(side_y > side_x and side_y > side_z):
        largest_side = side_y
    else:
        largest_side = side_z

    #Finds the smallest side
    if (side_x < side_y and side_x < side_z):
        smallest_side = side_x
    elif(side_y < side_x and side_y < side_z):
        smallest_side = side_y
    else:
        smallest_side = side_z

    #Finds the middle length side
    if (largest_side != side_x or smallest_side != side_x):
        medium_side = side_x
    elif (largest_side != side_y or smallest_side != side_y):
        medium_side = side_y
    else:
        medium_side = side_z
    
    #Finds the smallest angle
    if (ang_x < ang_y and ang_x < ang_z):
        smallest_angle = ang_x
    elif(ang_y < ang_x and ang_y < ang_z):
        smallest_angle = ang_y
    else:
        smallest_angle = ang_z
    
    while(correct_triangle == False):

        #Checks to see if the largest sides are opposite the largest angles
        if ((largest_side == side_x and largest_angle != ang_y) or (largest_side != side_x and largest_angle == ang_y)):
            print("The largest angle (Y) must have the largest side (X) opposite it")
            break
        elif((largest_side == side_y and largest_angle != ang_z) or (largest_side != side_y and largest_angle == ang_z)):
            print("The largest angle (Z) must have the largest side (Y) opposite it")
            break
        elif((largest_side == side_z and largest_angle != ang_x) or (largest_side != side_z and largest_angle == ang_x)):
            print("The largest angle (X) must have the largest side (Z) opposite it")
            break

        #Check to see if the smallest side is opposite the smallest angle
        elif((smallest_side == side_x and smallest_angle != ang_y) or (smallest_side != side_x and smallest_angle == ang_y)):
            print("The smallest angle (Y) must have the smallest side (X) opposite it")
            break
        elif((smallest_side == side_y and smallest_angle != ang_z) or (smallest_side != side_y and smallest_angle == ang_z)):
            print("The smallest angle (Z) must have the smallest side (Y) opposite it")
            break
        elif((smallest_side == side_z and smallest_angle != ang_x) or (smallest_side != side_z and smallest_angle == ang_x)):
            print("The smallest angle (X) must have the smallest side (Z) opposite it")
            break

        #Checks whether the sides add up to 180
        elif(ang_x + ang_y + ang_z != 180):
            print("The angles of a triangle must add up to 180. ")
            break

        #Checkes whether the triangle is obtuse, right or acute
        elif(ang_x > 90 or ang_y > 90 or ang_z > 90):
            obtuse_triangle = True
        elif(ang_x == 90 or ang_x == 90 or ang_x == 90):
            right_triangle = True
        else:
            acute_triangle = True

        
        #Checks whether length of a side is smaller than the sum of the other two
        if(side_x >= side_y + side_z):
            print("The length of side X must be smaller than the sum of the other two.")
            break
        elif(side_y >= side_x + side_z):
            print("The length of side Y must be smaller than the sum of the other two.")
            break
        elif(side_z >= side_y + side_x):
            print("The length of side Z must be smaller than the sum of the other two.")
            break

        #Checks whether the pythagorean theorem is held true
        if obtuse_triangle == True:
            if(largest_side**2 < medium_side**2 + smallest_side**2):
                print("That doesn't follow the pythagoream theorem for obtuse triangles!")
                break
        elif right_triangle == True:
            if(largest_side**2 != medium_side**2 + smallest_side**2):
                print("That doesn't follow the pythagoream theorem for right triangles!")
                break
        elif acute_triangle == True:
            if(largest_side**2 > medium_side**2 + smallest_side**2):
                print("That doesn't follow the pythagoream theorem for acute triangles!")
                break

        correct_triangle = True
        forward(side_x) 
        setheading(180 - ang_x)
        forward(side_y)
        setheading(180)
        left(ang_y)
        forward(side_z)
        setheading(180 - ang_z)  

#Use this to draw a perfect diamond
def diamond(units):
    setheading(45)
    forward(units)
    left(90)
    forward(units)
    left(90)
    forward(units)
    left(90)
    forward(units)
    left(90)

#Use this to draw a perfect pentagon
def pentagon(units):
    forward(units)
    left(108)
    forward(units)
    left(108)
    forward(units)
    left(108)
    forward(units)
    left(108)
    forward(units)
    left(108)
    
    
    
