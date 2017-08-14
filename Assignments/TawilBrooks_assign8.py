#8/6/14
#Brooks Tawil
#assignment 8
#

import random

#Creates a list of 100 slots for the amounts of the 100 donations
donations = [0]*100

#Creates a list of 100 that will assign which charity go the donation
charity = [0]*100

#Creates a list of 15 positions that will accumulate all of the donations for each charity
total_donations = [0]*15

#creates a list of 15 positions that counts how many times a charity recieves a donation
count_donations = [0]*15

#creates a list that will store the total average of each charity
charity_avg = [0]*15

for i in range(100):
    #creates random money donation
    rand_donation = random.randint(100,10000)
    rand_donation = rand_donation/100
    donations[i] = rand_donation

    #creates random charity to give the money to
    rand_charity = random.randint(0,14)
    charity[i] = rand_charity

    #accumulates the amount of money given to each charity
    total_donations[rand_charity] += rand_donation

    #adds one to the counter of the charity that recived the current donation
    count_donations[rand_charity] += 1

    #prints out what the current donation is and to what charity
#    print("A",donations[i],"dollar donation was given to charity #",charity[i] + 1)


for i in range(15):
    charity_avg[i] = total_donations[i]/count_donations[i]
    print("Charity #",i + 1,"recived a total of $%.2f" % total_donations[i],"with an average of $%.2f" % charity_avg[i],"per donation.")

for i in range(100):
    if (donations[i] < charity_avg[charity[i]]):
        print('Donation',i+1,'was $%.2f' % donations[i],'. It was below the average for charity #',charity[i],'by $%.2f' % (charity_avg[charity[i]] - donations[i]))
    elif (donations[i] > charity_avg[charity[i]]):
        print('Donation',i+1,'was $%.2f' % donations[i],'. It was above the average for charity #',charity[i],'by $%.2f' % (donations[i] - charity_avg[charity[i]]))
    else:
        print('Donation',i+1,'was $%.2f' % donations[i],'. It was equal to the average for charity',charity[i])












