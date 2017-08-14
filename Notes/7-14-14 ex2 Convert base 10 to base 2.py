#7/14/14
#Convert base 10 to base 2

num1 = int(input("Give me a base 10 number between 0 and 31"))

#start to convert

#1place
place1 = num1 % 2
num2 = num1 // 2

#2place
place2 = num2 % 2
num3 = num2 // 2

#4th place
place4 = num3 % 2
num4 = num3 // 2

#8th place
place8 = num4 % 2
num5 = num4 // 2

#16 place
place16 = num5 % 2
num6 = num5 // 2


print("Your binary number is",place16,place8,place4,place2,place1)
