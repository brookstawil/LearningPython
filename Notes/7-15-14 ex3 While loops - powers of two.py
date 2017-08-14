#7/15/14
#while loops - powers of two

power = 0

#print the powers of 2 from 2^0 to 2^16

#while (power <= 16):
#    print("2 to the power of",power,"is",2**power)
#    power += 1


# powers of two less than one million

while 2**power < 1000000:
    ans = 2**power
    print("2 to the power of",power,"is",ans)
    power += 1
