#7/28/14
#Midterm review
#Create fifty random integers from 1 - 1000, find total and average

import random

#Counters
rand_int_amt = 0
rand_int_sum = 0
largest_rand_int = -99999 #So low anything is greater
smallest_rand_int = 99999 #So low anything is smaller

#loop
for num in range(50): #Remember in range() gives us number s 0-49 inclusive, it is still fifty numbers though
    rand_int = random.randint(1,1000)
    print(rand_int)
    if rand_int > largest_rand_int:
        largest_rand_int = rand_int
    if rand_int < smallest_rand_int:
        smallest_rand_int = rand_int
    rand_int_sum += rand_int
    rand_int_amt += 1

#prints total
print("The sum of all the numbers is",rand_int_sum)

#Prints smallest number
print("The smallest number is",smallest_rand_int)

#print the largest number
print("The largest number was",largest_rand_int)

#average
avg_of_nums = rand_int_sum / rand_int_amt

#prints the average
print("The average number is %.2f" % avg_of_nums)
