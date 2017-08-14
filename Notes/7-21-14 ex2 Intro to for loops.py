#7/21/14
#intro to for loops
#Note: Any for loop can be translated to a while loop with a counter

#while loops need a counter to stop,
num = 0
while num < 4:
    print(num)
    num +=1

#for loops are a short hand that INCLUDES a counter

#for loop (with range function)
for num in range(4): #The range() function gives all numbers from 'num' to '4'
    print(num)

#The range() function is NOT inclusive at the Y perameter

#for loop (with range parameters)
for num in range(3,22): #The range(x,y) function gives all numbers from 'x' to 'y'
    print(num)

#for loop (with range perameters up by 3s)
for num in range(3,22,3): #The range(x,y,z) function gives all numbers from 'x' to 'y' up by 'z's
    print(num)

#for loop (with range perameters down by 3s)
for num in range(3,22): #The range(x,y,-z) function gives all numbers from 'x' to 'y' down by 'z'
    print(num)

#for loop (with sequence in a list)
for num in [1,2,3,6,2,4,6,3,21,-88]:
    print (num)











    
