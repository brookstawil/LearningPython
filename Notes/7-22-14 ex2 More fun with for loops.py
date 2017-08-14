#7/22/14
#More fun with for loops
#practice changing for loops to while loops and vice versa

#pick a random year 1800-1995
#print out the 20 years starting with that year

import random

random_year = random.randint(1800,1995)

counter = 0

while (counter < 20):
    print(random_year)
    random_year += 1
    counter += 1

year_to_print = str(random_year)

#You can make an index out of any varible that grabs the individual characters in a string
for alpha in year_to_print:
    print(alpha)
