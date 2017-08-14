#7-14-14
#Letter grades

#Input the grade
grade = input("What is the grade? ")

grade = grade.upper()

#Long way

#if grade == "A":
#    print ("A - Excellent")
#else:
 #   if grade == "B":
  #      print("B - good!")
   # else:
    #    if grade == "C":
     #       print("C - average")
      #  else:
       #     print =(grade,"other")

#Short way

#elif combines the else and if statement
if grade == "A":
    print("A - Excellent!")
elif grade == "B":
    print("B - Good!")
elif grade == "C":
    print("C - average")
