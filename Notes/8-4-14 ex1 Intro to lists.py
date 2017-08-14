#8/4/14
#Intro to lists

character = ["Hamlet","Falstaff","Ophelia","Julius Caesar","Portia",
             "Cleopatra","Learn","Caliban","Prospero","Viola"]

#REMEMBER LISTS START AT POSITION '0'!!!
print(character[2])

print(character[0])

position = 4
print(character[position])
print(character[position + 1])

howmany = len(character)

print('Last character of ' + str(howmany) + 'characters is ' + character[howmany - 1])

for letter in range(len(character)):
    print(letter,character[letter])

bunch_o_nums = [3,0,0,0,0,0,0,0,13,0,0,0,10]
print(bunch_o_nums)

count_nums = len(bunch_o_nums)
print('count o nums is',count_nums)

for pos in range(0,13):
    print(pos,bunch_o_nums[pos])

for place in range(13):
    print(place,bunch_o_nums[place])

x = bunch_o_nums[8]
print(x)

#If you give a negative postion it will read it right to left
print(character[-1])
print(character[-2])

for strange in range(-1,-11,-1):
    print(strange,character[strange])






