#7/31/14
#Determine whether a number (N) is prime or not
#We only have to check numbers up to the integer square root of N.

import math

#This determines whether n is prime
#INPUT - a number to check
#OUTPUT - Ture if it is prime or False if is is not

def is_prime(n):

    is_it_prime = True #We start with an assumption that it is prime

    divisor = 2 #This is the first divisor
    
    while (divisor <= math.sqrt(n)): #We use a while loop because we don't know how many iterations are needed
        #Is it divisible?
        if (n % divisor == 0): #Its divisible
            is_it_prime = False
            break     #Stops checking
        divisor += 1#Try the next divisor

    return is_it_prime

    
def main():

    how_many_primes = 1000
    counter_primes = 0
    n = 2
    while(counter_primes < how_many_primes):
        if is_prime(n) == True:
            counter_primes += 1
            print("%8d" % n,end = "")
        n += 1

main()
