#7/10/14
# Intro to the IF statement part 2

#remember input returns a string
age = int(input("How old are you?"))

print ("You are",age,"years old")

if age < 13:
    print ("You are a preteen")
else:
    print("You are old enough, back to the coal mines!!")
    if age < 19:
        print ("Wait are you a teenager? Get to the Iron Mines!!")
    else:
        print ("Make sure to forget about your miserable lives!!")
