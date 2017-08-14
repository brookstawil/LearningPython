#7/15/14
# Print out all GPA values from 4.00 to 0.00

GPA = float(4.00)

while GPA >= 0.00:
    print("%.2f" % GPA)
    GPA -= .01

#REMEMBER floating points need to be formatted
# "%.2f" is what is needed including quotations

