#7/30/14
#Read in a disk file

def main():

#Open the file for reading, This is also an internal name
    my_words = open('lyrics','r')

#Read the whole file(at one time)
    wholefile = my_words.read()

    print(wholefile) #Even the \n does its job

#Close the FILE!!!
    my_words.close()


main()
