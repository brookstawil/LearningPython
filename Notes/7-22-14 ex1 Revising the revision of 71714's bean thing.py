#7/22/14
#Revising the revision of 7/17/14's bean thing to work in a for loop

#7/17/14
#Revising exercise 3 so that it stops when you get 3 reds in a row

print("Let's pick some jelly beans!")

import random

#counter for how many times the loop has executed
counter = 0

#This allows for easy change of the amount of concecutive beans wanted
beans_con = 7

#counters for each color
red_count = 0
white_count = 0
blue_count = 0

#counters for concecutive picks of beans ('con' stands for 'concecutive')
red_con_count = 0
white_con_count = 0
blue_con_count = 0

#all runs total bean count
tot_beans_all_runs = 0

max_num_trials = 3
for num_trials in range(max_num_trials):

####### Starts running the problem one time

    #To switch which color simply change the color in front of '_con_count'
    while (red_con_count < beans_con):

        #determines what bean is picked
        ran_color = random.randint(1,3)

        #adds 1 to counter
        counter += 1
        
        if (ran_color == 1):
            #print("You got red")
            red_count += 1
            #adds one to the red consecutive count 
            red_con_count += 1
            #removes consecutive count from other colors
            white_con_count = 0
            blue_con_count = 0
        elif (ran_color == 2):
            #print("You got white")
            white_count += 1
            #adds one to the white consecutive count
            white_con_count += 1
            #removes consecutive count from other colors
            red_con_count = 0
            blue_con_count = 0
        else:
            #print("You got blue")
            blue_count += 1
            #adds one to the blue consecutive count
            blue_con_count +=1
            #removes consecutive count from other colors
            red_con_count = 0
            white_con_count = 0

        num_picks = white_count + blue_count + red_count

    print("You got",beans_con,"consecutive red beans after",counter,"tries")

    tot_beans_all_runs = tot_beans_all_runs + counter

####### Ends running the problem one time
