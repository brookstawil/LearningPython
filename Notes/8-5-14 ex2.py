#8/5/14
#Array countdown

N = int(input('Give me a number to countdown from. '))

mylist = [0] * (N+1)

#print(mylist)

for pos in range(N,0,-1):
    mylist[N - pos] = pos

print(mylist)


