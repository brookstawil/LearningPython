#7/15/14
#Brooks Tawil Assignment 2
#This program will determine whether a given date is an NYU holiday.

print("This program will determine whether a given date is an NYU holiday for the 2014-15 academic year. ")

#getting user inputs
month = int(input("Please enter the month's numerical value "))
day = int(input("Please enter the date "))

#Error messages
#The while loops will stop the program from running until the user puts in a valid month and day

#invalid month
while month > 12 or month < 1:
        print("That is NOT a valid MONTH, please try again")
        month = int(input("Please enter the month's numerical value "))
        day = int(input("Please enter the date "))
    

#invalid day
while day > 31 or day < 1:
        print("That is NOT a valid DAY, please try again")
        month = int(input("Please enter the month's numerical value "))
        day = int(input("Please enter the date "))

#"if the month has 30 days instead of 31" error
while (month == 4 or month == 6 or month == 9 or month == 11) and day == 31:
        print("That month doesn't have 31 days, please try again")
        month = int(input("Please enter the month's numerical value "))
        day = int(input("Please enter the date "))

       
#"Febuary only has 28 days" error
while (month == 2) and (day > 28):
        print ("Febuary only has 28 days, please try again")
        month = int(input("Please enter the month's numerical value "))
        day = int(input("Please enter the date "))

#Now we check to see if the date is a holdiay

#Labor Day
if (month == 9) and (day == 1):
    print(str(month) + "/" + str(day) + " is Labor Day.")
#Academic Holiday
elif (month == 10) and (day == 13 or day == 14):
    print(str(month) + "/" + str(day) + " is an Academic Holiday")
#Thanksgiving
elif (month == 11) and (day >= 27 and day <= 30):
    print (str(month) + "/" + str(day) + " is Thanksgiving")
#Winter recess
elif ((month == 12) and (day >=20 and day <= 31)) or ((month == 1) and (day >= 1 and day <= 26)):
    print (str(month) + "/" + str(day) + " is during Winter recess")
#Presidents' Day
elif (month == 2) and (day == 16):
    print (str(month) + "/" + str(day) + " is Presidents' Day")
#Spring recess
elif (month == 3) and (day >= 16 and day <= 22):
    print(str(month) + "/" + str(day) + " is during Spring recess")
#Memorial Day
elif (month == 5) and (day == 25):
    print(str(month) + "/" + str(day) + " is Memorial Day")
#Independence Day
elif (month == 7) and (day == 6 or day == 7):
    print(str(month) + "/" + str(day) + " is Indeppendence Day ")
#Summer Recess
elif (month == 8) and (day >= 15 and day <= 31):
    print(str(month) + "/" + str(day) + " is during summer recess")
else:
    print(str(month) + "/" + str(day) + " is NOT a school holiday. ")
