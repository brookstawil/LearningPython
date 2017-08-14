#7-14-14
#Problem: Figure out whether an inputted number is a vowel

letter = input("What letter would you like to look at? ")
letter = letter.upper()

if letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
    print("The letter",letter,"is a vowel")
else:
    print("The letter",letter,"is a concenant")
