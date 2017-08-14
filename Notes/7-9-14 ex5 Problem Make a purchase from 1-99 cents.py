#7/9/14
#Problem: Make a purchase from 1-99 cents

#Compute the minimum number of coins for the change from 1$

cost = int(input("How many cents does it cost?"))
change = 100 - cost
print (change,"cents is your change")

#quarters
quart_amt = change // 25
remainder = change % 25
#print (remainder)
#print ("You get back ",quart_amt,"quarters(s)")

#dimes
dime_amt = remainder // 10
remainder = remainder % 10
#print (remainder)
#print ("You get back",dime_amt,"dime(s)")

#nickels
nick_amt = remainder // 5
remainder = remainder % 5
#print (remainder)
#print ("You get back",nick_amt,"nickle(s)")

#pennies
penn_amt = remainder // 1
remainder = remainder % 1
#print (remainder)
#print ("You get back",penn_amt,"penny(ies)")

print ("You get back",quart_amt,"quarter(s),",dime_amt,"dime(s),",nick_amt,"nickel(s) and",penn_amt,"penny(ies)")



