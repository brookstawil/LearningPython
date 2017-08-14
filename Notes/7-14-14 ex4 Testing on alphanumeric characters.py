#7-14-14
#Testing on alphanumeric characters

letter = input("Please type in a single alphabetical character. ")

#print(letter)
#The .upper() function gives the uppercase version of the character
letter = letter.upper()
#print(letter)

if len(letter) > 1:
    print("ERROR! Type in a SINGLE letter")
else:
    if letter == "C":
        print("HAHA you found today's sece=ret letter!!")
    else:
        print("Sorry you didn't get today's secret letter, try again")

if letter >= "A" and letter <= "Z":
    print("But it IS a letter!")
else:
    print("Its not even A letter!")
   


