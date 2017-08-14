# 7/9/14 Ex4
#Problem: Input a four digit number

#Output: Each number on a separate line

num = int(input("What is the four digit number?"))

#1st digit
thousands = num // 1000
print("The first digit is",thousands)

#2nd digit
remainder = num % 1000
#print(remainder)
hundreds = remainder // 100
print ("The second digit is ",hundreds)

#3rd digit
remainder = num % 100
#print(remainder)
tens = remainder // 10
print ("The third digit is ",tens)

#4th digit
remainder = num % 10
#print(remainder)
ones = remainder
print ("The fourth digit is ",ones)

