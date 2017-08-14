#7/16/14
#Fibonacci numbers with loops
#problem determine the fibonacci numbers up to an inputed number

#Defined starting numbers
num_n1 = 1
num_n2 = 0
fib_num = num_n1 + num_n2
#User input
num_user = int(input("Number? "))
counter = 1

#Loop
print("All subsequent numbers follow from the first two defined terms: 0 and 1")

while (fib_num < num_user):
    print("The",counter,"fibonacci number is",fib_num)
    num_sum = num_n1 + num_n2
    fib_num = num_sum
    num_n2 = num_n1
    num_n1 = fib_num
    counter += 1

if (fib_num > num_user):
    print("The number",num_n2,"is the largest fibonacci number able to be subtracted into",num_user)
        
    
    
    
    

    
    
    


    
    
    
