#7/14/14
#Read in a # determine if its even or odd

num1 = int(input("Type in an integer:"))

#print("Your number is",num1)

#num2 = num1 + 1

#determine if it is even or odd

#"==" is what we know as "equal", its not an assignment but rather a boolean check
if (num1 % 2) == 0:
    print(num1,"is an even integer")
else:
    print(num1,"is an odd integer")

