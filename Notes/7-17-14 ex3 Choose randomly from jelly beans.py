#7/17/14
#pick random colors
#Choose 100 red, white or blue jellybeans and count them

import random

#how many you pick
numpicks = int(input("How many beans do you want to pick from the infinit bean machine? "))

#counters for each color
red_count = 0
white_count = 0
blue_count = 0

#counter for the while loop
bean_counter = 0

while (red_count < 5):
    ran_color = random.randint(1,3)

    #changes color integers to strings
    #red
    if ran_color == 1:
    #    print("You got a red jelly bean!")
        red_count += 1
    #white
    elif ran_color == 2:
    #    print("You got a white jelly bean!")
        white_count += 1
    #blue
    else:
    #    print("You got a blue jelly bean!")
        blue_count += 1

    #sets up for next iteration(goes last)
    bean_counter += 1
    
#print the results! and percents!
#red
print("You got",red_count,"red jelly beans")
red_percent = 100 * (red_count / bean_counter)
print("The percent of red jelly beans was",str(red_percent) + "%.")
#white
print("You got",white_count,"white jelly beans")
white_percent = 100 * (white_count / bean_counter)
print("The percent of white jelly beans was",str(white_percent) + "%.")
#blue
blue_percent = 100 * (blue_count / bean_counter)
print("You got",blue_count,"blue jelly beans")
print("The percent of blue jelly beans was",str(blue_percent) + "%.")

    
