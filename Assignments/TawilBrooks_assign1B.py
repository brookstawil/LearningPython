#7/13/14
#Brooks Tawil Assignment 1B
#This program will determine whether an inputed year is a leap year or not.

#Asks for year
year = int(input("Which year which you wish to see?"))

#Negative number error
if year < 0:
    print ("ERROR! CAN NOT COMPUTE NEGATIVE YEARS!")


else:
    #If it is a century year NOT divisible by 400 it is NOT a leap year
    if year % 100 == 0 and year % 400 != 0:
        print("The year",year,"is NOT leap year.")

    else:

        #if it is divisible by 4 it is a leap year
        if year % 4 == 0:
            print("The year",year,"is a leap year.")

        #If its not divisible by 4 it is NOT a leap year
        else:
            print("The year",year,"is NOT a leap year.")
        
    
