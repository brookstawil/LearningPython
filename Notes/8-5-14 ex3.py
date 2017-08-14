#8/5/14
#Array of squares

N = int(input("Give us a number to use. "))

N +=1

mysquares = [0] *(N)

for place in range(N):
    mysquares[place] = place * place

print (mysquares)

#Now find the difference between any of the squares and the one to its left

for P in range(1,N):
    new_num = mysquares[P] - mysquares[P-1]
    print(new_num)
