#7/22/14
#Problem: First read in n = the number of stars to print
#Then print a column of n starts

num_stars = int(input("Input the number of stars. "))

num_spaces = 1

#Remember this technique
#Remember the 'end' staements!!!!
#As well as the ability to multiply stringsand make them repeat!!!!
for star in range(num_stars):
    print("*",end = "\n" + " "*num_spaces)
    num_spaces += 1

