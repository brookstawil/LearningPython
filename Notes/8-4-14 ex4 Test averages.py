#8/4/14
#Test averages

import random

num_students = 30

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

for num in range(0,num_students):
    if (scores[num] < avg):
        print("Student",num + 1,"got a",scores[num],"which was below average.")
    elif (scores[num] > avg):
        print("Student",num + 1,"got a",scores[num],"which was above average.")
    else:
        print("Student",num + 1,"got a",scores[num],"which was at the average.")

print(scores)



