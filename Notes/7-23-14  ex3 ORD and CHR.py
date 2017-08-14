#7/23/14
# ORD and CHR

alpha = "A"

#'ord' gives us what the ascii value is
num = ord(alpha)

print(alpha,num)

asciivalue = 122

#'chr' gives us which ascii character a value is
print(asciivalue," ",chr(asciivalue))

for number in range(65,123):
    print(chr(number),end="")
