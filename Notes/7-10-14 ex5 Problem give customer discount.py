#7/10/14
#Problem: If 100-249.99$ give 20% discount, greater is 30%

#input the cost of each item
purch1 = float(input("What is the price of the 1st item"))
purch2 = float(input("What is the price of the 2nd item"))
purch3 = float(input("What is the price of the 3rd item"))
purch4 = float(input("What is the price of the 4th item"))
purch5 = float(input("What is the price of the 5th item"))

#compute total
cost = purch1+purch2+purch3+purch4+purch5

#less than 100
if cost < 100:
    print ("The total cost is",cost)
    print ("Thank you have a nice day!")
else:
    print("Oh you get a special discount")
    if cost > 250
        print ("You get a megadiscount of",discount1,"dollars!")
        
    else
        print("You get a discount of",discount2,"dollars!")
