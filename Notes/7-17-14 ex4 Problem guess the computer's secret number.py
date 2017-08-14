#7/17/14
#Problem: guess the computer's secret number

import random

#computer number
cpu_num = random.randint(1,5)

#user guess
user_num = int(input("Guess the computer's number from 1-5! "))

#start counter
counter = 1

while (user_num != cpu_num):
    if (user_num < 1 or user_num > 5):
        counter += 1
        print("Only numbers 1-5! ")
        user_num = int(input("Guess the computer's number from 1-5! "))
    else:
        print("Sorry guess again")
        counter += 1
        user_num = int(input("Guess the computer's number from 1-5!"))

print("You guessed correctly! the secret number was",cpu_num,"and you guessed it in only",counter,"times!")    
