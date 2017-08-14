#7/19/14
#Assignment 3a
#This program will recieve an input for the amount of sides to dice
#It will out put the amount of tries it takes to get doubles three times

import random

#sides
sides = int(input("How many sides do your dice have? "))

#sets up a counter to see how many times the dice were rolled
times_rolled = 0

#sets up the varible for how many doubles are rolled
amt_doubles = 0

while(amt_doubles < 3):
    #Adds 1 to the amount of times rolled
    times_rolled += 1
    
    #Rolls the dice
    die1 = random.randint(1,sides)
    die2 = random.randint(1,sides)
    
    #Prints the roll number as well as the numbers rolled
    print("Roll #" + str(times_rolled) + ": You rolled a",die1,", and a",die2)
    
    #If the die rolls are equal
    if (die1 == die2):
        print("You got doubles!")
        amt_doubles += 1

    #Once you reach 3 doubles you stop
    if (amt_doubles == 3):
        print("Hooray! You got doubles three times! It took",times_rolled,"times to get it.")

    
