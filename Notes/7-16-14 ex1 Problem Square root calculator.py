#7/16/14
#Problem: See how many odd integers can be subtracted from a given number
#Believe it or not this actually gives the square root, the amount of integers need is the square root!!

#number input
num = int(input("Give me a number to square root! "))
num_begin = num
#Loops through the subtractions

#defines the start number we are subtracting num with
#It also defines the start of the count for how many integers are needed
subtracter = 1
ints_needed = 1

#Commenting out the print statements SIGNIFICANTLY increases speed
#Loop
while (num > subtracter):
    print(str(ints_needed) + ": The odd integer used is " + str(subtracter))
    num = num - subtracter
    subtracter += 2
    ints_needed += 1
    
    

#Prints the amount of integers needed
print(str(ints_needed),"odd integers were needed ending at " + str(subtracter) + " which would make the number negative")
print("The square root of",num_begin,"is",ints_needed)
