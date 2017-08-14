#8/4/14
#Lists: rolling a die
#Count the number of times each side comes up

import random

def main():
#    s1 = 0
#    s2 = 0

    die = [0,0,0,0,0,0,0] #positions 0-6 but wont use position 0, we want numbers 1-6
    num_rolls = 10000

    for rolls in range(num_rolls):
        side = random.randint(1,6) #generates 1-5
        #if side = 1:
        #   die[1] == die[1] + 1

        die[side] += 1 #simplified of the above, adds oone to a certain position in the list

    for num in range(1,7): #generates 1-6
        print('You rolled a',num,die[num],"times")

    
main()
