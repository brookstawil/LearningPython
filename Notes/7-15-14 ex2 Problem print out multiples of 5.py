#7/15/14
#print out the multiples of 5 from 5 to 200


num = 5

print("The multiples of 5 up to 200 are:")

while (num <= 200):
    if num % 5 == 0:
        print (num)
    # "+=" is the same as "num = num +"
    num += 5

phrase = str("LOL!")
i = 0
while i <= 100:
    print (phrase)
    i += 1
