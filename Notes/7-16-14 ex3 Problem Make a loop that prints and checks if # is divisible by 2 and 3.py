#7/16/14
#Problem: Make a loope that prints out integers and tells you whether that integer is divisible by 2 and three from 1 - 100

#starting number
numA = 1
numB = 1
counter = 1

while (counter <= 100):
    #checks if divisible by 2
    if (numA % 2 == 0):
        print(numA,"is divisible by 2", end = "")
        counter += 1
        numA += 1
    else:
        print(numA,"is NOT divisible by 2", end = "")
        counter +=1
        numA += 1
    #checks if divisible by 3
    if (numB % 3 == 0):
        print(",its divisible by 3")
        numB += 1
        
    else:
        print(",its NOT divisible by 3")
        numB += 1
