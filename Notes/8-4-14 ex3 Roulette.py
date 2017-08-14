#8/4/14
#Roulette

import random

def main():

    die = [0]
    die = die*37 #now you have position 0-36

    num_spins = 1000
    
    for spin in range(num_spins):
        side = random.randint(0,36)

        die[side] += 1

    print(die)

    for s in range(1,37):
        print("You spun a",s,die[s],"times.")

main()
