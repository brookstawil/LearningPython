#7/23/14
#Intro to functions

import random

#We define the function 
def cap_letter():
    cap = chr(random.randint(65,90))
    print(cap,end="")

#Then we can run it as we please
#for num in range(3):
#    cap_letter()

def vowel():
    vowel = random.choice("aeiou")
    print(vowel,end="")

def lower_letter():
    low = chr(random.randint(97,122))
    print(low,end="")


#lets do a whole word
def print_word():
    cap_letter()
    vowel()
    lower_letter()
    lower_letter()

    print()

def main():
    for num in range(20):
        print_word()

main()
