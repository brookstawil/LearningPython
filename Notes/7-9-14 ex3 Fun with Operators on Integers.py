# 7/9/14
# Fun with Operators on Integers


#inputs ONLY give back strings so we must convert it to integers with 'int'
input_age = input("Type your age")
age = int(input_age)
print("Your age is", age)

age_next_year = age + 1

print("Your age next year will be ",age_next_year)

twice_age = age * 2
print ("2x your age is ",twice_age)

#half_age = age / 2
#A '/' gives back floating numbers
#print("Half your age is", half_age)

halfage_int = age // 2
#We need two /s to define the number as an integer
print("Half your age is",halfage_int)

remainder = age % 2
# % is a mod operator, divides number and returns ONY the remainder
print ("with ", remainder, " years left over")
