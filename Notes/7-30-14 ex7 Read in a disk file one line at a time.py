#7/30/14
#Read in a disk file One line at a time

def main():

#Open the file for reading, This is also an internal name
    my_words = open('lyrics','r')

#Read one line at a time
    line_count = 0
    one_line = my_words.readline() 

    while(one_line != ""): #stop when you get an empty line
        line_count += 1
        one_line = one_line.rstrip("\n") #.rstrip() will remove the specified characters from a string
        print("Line #",line_count, one_line)
        one_line = my_words.readline() #.readline() will read it line by line
    
    print("That's all folks")
     
#Close the FILE!!!
    my_words.close()


main()
