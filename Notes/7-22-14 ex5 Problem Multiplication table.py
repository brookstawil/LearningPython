#7/22/14
#Problem: Print out a multiplication table

#table #1

#for fact1 in range(1,11):

#    for fact2 in range(1,11):
#        product = fact1 * fact2
#        print("%d * %2d = %3d" %(fact1, fact2, product))

#This uses a double nested for loop!

#What we really want is an old fashioned table!

#    1    1    1    1    1    1
#  x 1  x 2  x 3  x 4  x 5  x 6
# ---- ---- ---- ---- ---- ----
#    1    2    3    4    5    6


#Look this over for the midterm
#Loops can be nested over and over
#They can be used to format things like this
for fact1 in range(1,11):
    for fact2 in range(1,11):
        print("%5d" % fact1,end="")
    print()

    for fact2 in range(1,11):
        print(" x %2d" % fact2,end="")
    print()

    print("  ---"*10)

    for fact2 in range (1,11):
        product = fact1 * fact2
        print("  %3d" % product,end="")

    print("\n")
        
