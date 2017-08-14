#7/24/14
# Functions with perameters

#compute squares and cubes

def print_square(i): #The variable 'i' is LOCAL when it is a parameter. Parameters are only known to the function they are used in
    ans = i**2
    return ans #The return command brings back the answer into the program to be used in other functions

def print_cube(q):
    c = q**3
    return c

def main():
    sq = print_square(4)

    sq = print_square(3)

    num = 12

    sq = print_square(num + 7)
    sq = print_cube(num + 7)

    #Eventhough the main function uses 'i' it is LOCAL or known only to print_square()
    #print(i)

    for numbah in range(20):
        da_square = print_square(numbah)
        print("*****",da_square)
        da_cube = print_cube(numbah)
        print("*****",da_cube)
main()
