#7/31/14
#Use your name in substrings
#Single line for name
#If only gives one name print error
#Print out the first and last name on separate lines

#The name
name = input("What is your first and last name? ")

#length of the name
length = len(name)
position = 0
substring = name[0: length: 1]
one_name_only = True

while position < length and one_name_only:
    if name[position] == " ":
        one_name_only = False
    else:
        position += 1

if one_name_only == True:
    print("Error please give your last name")
else:
    print("The space was found at position",position)

    first_name = name [0: position]
    last_name = name[position + 1: length]

    print(first_name)
    print(last_name)

