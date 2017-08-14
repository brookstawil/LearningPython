#7-14-14
#Fun with functions, intro to libraries

#This pulls functions from the "MATH" library, allowing us to use those functions

import math

radius1 = float(input("What is the radius of the circle? "))

#The %5.2f reserves AT LEAST 5 spaces for the number wikth 2 after the decimal
print("Given the radius of %5.2f for the cirle," % radius1)

area = math.pi * math.pow(radius1, 2) #same as radius1 ** 2

print("The area is %.3f" % area)
