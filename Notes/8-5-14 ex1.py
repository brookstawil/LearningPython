#8/5/14
#Revising 8/4/14 ex4

import random

num_students = 19

scores = [0]*num_students #20 positions for tests
total = 0

for student in range(num_students):
    test = random.randint(0,100)
#    print("Student #" + str(student + 1),"got a",test)
    scores[student] += test
    total += test

print('The total amount of points was',total)
avg = total // num_students
print('The average was a',avg)

##for num in range(0,num_students):
##    
##    if (scores[num] < avg):
##        print("Student",num + 1,"got a",scores[num],"which was below average.")
##    elif (scores[num] > avg):
##        print("Student",num + 1,"got a",scores[num],"which was above average.")
##    else:
##        print("Student",num + 1,"got a",scores[num],"which was at the average.")

every_other_total = 0

for position in range(0,num_students,2):
    every_other_total += scores[position]
    print(position + 1,scores[position])

print("Every other student got a total of",every_other_total)

highest_score = -9999
highest_score_counter = 0

for student in range(num_students):
    if (scores[student] > highest_score):
        highest_score != scores[student]
        highest_score = scores[student]
        highest_score_counter = 1
    elif (scores[student] == highest_score):
        highest_score_counter += 1

print(highest_score_counter,"student(s) got a",highest_score,",the highest score")

print(scores)



