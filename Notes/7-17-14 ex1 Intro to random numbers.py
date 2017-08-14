#7/17/14
#Intro to random numbers

import random

#random.readin(a,b)
#this function returns a random integer, n, such that a <= n <= b

#random card
rand_card = random.randint(1,52)
print(rand_card)

#random die roll
rand_die = random.randint(1,6)
print(rand_die)

#random year between 1900 and 2000
#Note the two numbers in the function are INCLUSIVE
rand_year = random.randint(1900,2000)
print(rand_year)

#random floating point number
rand_float = random.random()
print(rand_float)
