#7/31/14
#Fun with sub strings

def main():
    thestring = input("Type a message")
    length = len(thestring)

    print("Your string has",length,"characters")

    first = thestring[0]

    last = thestring[length - 1]

    print("The first character is",first,"and the last character is",last)

    start = int(input("Where do you want your substring to start? "))
    stop = int(input("Where do you want your substring to stop?"))
    step = int(input("How much do you want to step up by? "))

    newstring = thestring [ start: stop: step]

    print("Your substring is:",newstring)

main()
