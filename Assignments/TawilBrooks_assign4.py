#7/22/14
#Brooks Tawil assignment 4
#This program deals out random cards from a consistently fresh deck and also gives you how many face cards were dealt

import random

#sets up a counter for the amount of face cards
face_amt = 0

for num in range(0,53):


    #Determines suit
    suit = random.randint(1,4)

    #Gives string value to the suits
    if (suit == 1):
        suit = "Clubs"
    elif (suit == 2):
        suit = "Hearts"
    elif (suit == 3):
        suit = "Diamonds"
    else:
        suit = "Spades"

    #Determines rank
    rank = random.randint(1,13)

    #Gives string value to face cards and ace
    if (rank == 1):
        rank = "Ace" 
    elif (rank == 11):
        rank = "Jack"
        face_amt += 1
    elif (rank == 12):
        rank = "Queen"
        face_amt += 1
    elif (rank == 13):
        rank = "King"
        face_amt += 1

    print("You got a",rank,"of",suit)

print("Out of the 52 cards dealt,",face_amt,"of them were face cards")


