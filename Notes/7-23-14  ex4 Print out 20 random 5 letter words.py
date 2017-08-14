#7/23/14
#Print out 20 random 5 letter word with:
#uppercase,vowel,lowercase,lowercase

import random

for words in range (20):
#capital letter
    cap = chr(random.randint(65,90))

    print(cap,end="")
#vowel
#    vowel = random.randint(1,5)
#   if vowel == 1
#        print("a",end="")
#   elif vowel == 2:
#       print("e",end="")
#   elif vowel == 3:
#       print("i",end="")
#  elif vowel == 4:
#        print("o",end="")
#   else:
#       print("u",end="")

vowel = random.choice("aeiou"):
    print(vowel,end="")

#lowercase1

    low = chr(random.randint(97,122))

    print(low,end="")

#lowercase2

    
    low = chr(random.randint(97,122))

    print(low)
