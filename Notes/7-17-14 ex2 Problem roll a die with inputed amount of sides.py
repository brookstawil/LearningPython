#7/17/14
#Problem: roll a die with inputed amount of sides

import random

sides = int(input("How many sides does the die have? "))

rand_num = random.randint(1,sides)
die1 = rand_num
die2 = rand_num

die_sum = die1 + die2
print("You rolled a",die_sum,"on a",sides,"sided die with a",die1,"and a",die2)
