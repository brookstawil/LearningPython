#8/5/14
#Let it rain!!

import random

num_stu = 20
num_bills = 10
amt_per_bill = 100

money = [0]*num_stu

for bill in range(num_bills):

    which_stu = random.randint(0,num_stu - 1)
    #We chose a student now we choos an amount
    which_bill = random.randint(1,4)
    if which_bill == 1:
        amt_per_bill = 20
    elif which_bill == 2:
        amt_per_bill = 50
    else:
        amt_per_bill = 100

    which_stu = random.randint(0,num_stu - 1)
    print('student',which_stu,'won $',amt_per_bill)
    money[which_stu] += amt_per_bill

for stu in range(num_stu):
    print('student',stu,'has a grand total of $',money[stu])

#Now we print the max and who got it

maximum = 0

for stu in range(num_stu):
    if money[stu] > maximum:
        maximum = money[stu]

print('The maximum winnings was $',maximum,'which was won by student number(s)',end='')

for stu in range(num_stu):
    if money[stu] == maximum:
        print(stu,end=" ")
