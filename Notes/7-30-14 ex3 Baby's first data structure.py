#7/30/14
# String - Our first data structure

def main():

    msg = input("Type in your secret message. ")

    for letter in msg:
        print(letter + " " + str(ord(letter)) + " " +  chr(ord(letter)))

    how_long = len(msg)
    print("The message was",how_long,"characters long")
    print("The first character in the message was",msg[0]) #Here we are asking for the position in the string, the first position is position 0
    print("The last character in the message was",msg[how_long - 1])

    position = 0
    while(position < how_long):
        print( msg[position])
        position +=1

    print("Every third character is")
    position = 0
    while(position < how_long):
        print( msg[position])
        position += 3

main()
