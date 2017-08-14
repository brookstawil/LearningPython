#7/30/14
#Write a text file to the disk

def main():

#Open a file, this is an internal name, not the OS name of the file
    opera_file = open("lyrics","w")
    
#Write some stuff to the file
    opera_file.write("\nH.M.S. Pinafore\n")
    opera_file.write("When I was a lad I served a term\n")
    opera_file.write("As office boy to an attorny's firm\n")
    opera_file.write("I cleaned the windows and I swept the floors\n")
    opera_file.write("And I polished up the handle on the big front door\n")

#Close the FILE!!!!!
    opera_file.close()

    print("File successfully written")

main()
