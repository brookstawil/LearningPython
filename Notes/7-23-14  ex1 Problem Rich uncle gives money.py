#7/22/14
#Problem:Rich uncle gives money, make requests for purchases until over 1000

#How much you want to spend
user_num = float(input("What amount of money do you want to spend? "))

#starting budget
uncle_money = 1000.00

#amount spent counter
amt_spent = 0

#counters for purchases
amt_purchases = 0

while (uncle_money >= user_num):
    amt_spent += user_num
    uncle_money -= user_num
    print("You just purchased a ",user_num,"dollar item!")
    print("You have ",uncle_money,"dollars left. ")
    user_num = float(input("What amount of money do you want to spend? "))
    amt_purchases +=1

#Cant make the purchase, what were your shoping stats
print("You only have ",uncle_money,"dollars left, sorry you can't make that purchase! ")
print("You made a total of",amt_purchases,"purchases")
print("You spent a total of ",amt_spent,"dollars.")

#Calculate averages
if amt_purchases > 0:
    avg_per_purchase = amt_spent / amt_purchases
    print("You spent an average of ",avg_per_purchase,"on your purchases")

else:
    print("You didn't even make any purchases to average together!")
