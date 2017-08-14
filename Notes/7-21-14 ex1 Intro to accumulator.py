#7/21/14
#Intro to accumulator

#The grocery cart
#Buy EXACTLY 5 items

num_items = 0

#How many items
#total_items = int(input("How many items do you have sir? "))

clerk_ans = 0

#starting cost
total = 0.00

amt = input("Type the cost of the first item (or STOP)")

while (amt != "STOP"):
    num_items += 1
    amt = float(amt)
    print(amt)    

    total = total + amt

    print("Your running total is %3.2f" % total)

    amt = input("Type the cost of the next item (or STOP)")

    


print("Your grand total is $ %3.2f" % total)

#avg = total / total_items

#print("*** The average price per item is %3.2f" % avg)


#This uses 'accumulators', the running_total is INSIDE the loop
#To print the grand total you need it OUTSIDE the loop
