#7/17/14
#Assignment 3b
#This program will find the factorial of an inputed number

#User inputs number
user_num = int(input("Pick a number from 1-15 to factorialize. "))

#sets another variable to be used in calculations leaving user_num to be printed in the answer
num = user_num

#checks whether the number is from 1-15
while(num < 1 or num > 15):
    print("Only numbers from 1-15 are allowed")
    num = int(input("Pick a number from 1-15 to factorialize. "))

#num2 is defined so that it can be multiplied by num in the loop
num2 = num - 1

#sets the total to 1, total is the final answer that will be printed
total = 1

#ans is the answer to the current multiplication of numbers
#It then subtracts 2 from num so that it can be used to continue the factorial loop
while(num > 1): 
    ans = num2 * num
    num = num - 2
    num2 = num - 1
    total = ans * total

#This prints what the input is as well as the final answer
print("The answer to",str(user_num) + "! is",total)
