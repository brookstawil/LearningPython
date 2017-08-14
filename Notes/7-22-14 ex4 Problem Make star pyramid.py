#7/22/14
#Problem: Make a pyramid of stars!

num_lines = int(input("Stories do you want your pyramid to be? "))

#Number of stars per line, to be added on to in the loop
stars_per_line = 1

#Defines a counter for how many lines are used, to be added onto in

lines_counter = 1

#how many spaces
amt_spaces = num_lines - lines_counter

for row in range(num_lines):
    print(" "*amt_spaces + "*"*stars_per_line,row)
    stars_per_line += 2
    lines_counter += 1
    amt_spaces = num_lines - lines_counter

#Another method

for row in range(num_lines):
    print(" "*(num_lines - 1 - row) + "*"*(row*2 + 1))    
    
    

