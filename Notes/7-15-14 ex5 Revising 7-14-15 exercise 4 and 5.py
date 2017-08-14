#7/15/14
#Revising 7/14/15 exercise 4 and 5

letter = input("Please type in a single alphabetical character. ")

#The .upper() function gives the uppercase version of the character
letter = letter.upper()
#print(letter)

#Checks to see if you typed only a single 
while len(letter) != 1:
    print(letter)
    if (len(letter) >1):
        print("Too many letters try again")
    letter = input("Please type in a single alphabetical character. ")
    letter = letter.upper()


#Checks if its a letter
while letter <= "A" or letter >= "Z":
    print(letter)
    if letter <= "A" or letter >= "Z":
        print("Thats not a letter, try again.")
    letter = input("Please type in a single alphabetical character. ")
    letter = letter.upper()


#Checks if its the secret letter
if len(letter) > 1:
    print("ERROR! Type in a SINGLE letter")
else:
    if letter == "C":
        print("HAHA you found today's seceret letter!!")
    else:
        print("Sorry you didn't get today's secret letter, try again.")

#Shorter way to check for vowels
if letter in [ "A", "E", "I", "O", "U"]:
    print("The letter",letter,"is a vowel")
elif letter <= "A" or letter >= "Z":
    print()
else:
    print("The letter",letter,"is a consonant")
