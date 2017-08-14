#7/16/14
#Check the password 

password = "password" #really bad password

#password counter
counter = 1

guess = input("What is the password? ")

#You can also set the condition for the while loop as false
#As long as its false the program will run
#The wrong answer will change the value to true, stopping the loop
while (counter <= 3):
    #Get it right the loop stops
    if guess == password:
        print("Correct you may enter!")
        counter = 4
    #Get it wrong we add one to the counter until you get it right or until you un out of tries
    else:
        if (counter == 1):
            print("EHHH wrong answer try again")
            counter += 1
            guess = input("What is the password? ")
        elif (counter == 2):
            print("EHHH wrong answer one last try")
            counter += 1
            guess = input("What is the password? ")
        elif (counter == 3):
            print("YOU SHALL NOT PASS!!")
            counter += 1
