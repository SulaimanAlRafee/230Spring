#to comment many lines at once, you need to click:
  #<ctrl>+k  <ctrl>+c
#to uncomment many lines at once, you need to click:
  #<ctrl>+k  <ctrl>+u

#Student letter grade
grade = int(input("What's your total grade: "))
#1st method
if grade >= 90:
  print("Your letter grade is an A")
if grade >= 80 and grade < 90:
  print("Your letter grade is an B") 
if grade >= 70 and grade < 80:
  print("Your letter grade is an C")
if grade >= 60 and grade < 70:
  print("Your letter grade is an D") 
if grade < 60:
  print("Your letter grade is an F") 
#2nd method
if grade >= 90:
  print("Your letter grade is an A")
else:
  if grade >= 80:
    print("Your letter grade is an B") 
  else:
    if grade >= 70:
      print("Your letter grade is an C")
    else:
      if grade >= 60:
        print("Your letter grade is an D") 
      else:
        if grade < 60:
          print("Your letter grade is an F") 
print("Done")


#conversion of lengths
# print("Please select one of the following:")
# print("    convert from cm to in")
# print("    convert from in to cm")
# result = input("Please select cm or in: ")
# if result == "cm":
#   cm = int(input("How many cm?"))
#   inch = cm / 2.5
#   print("In inches, it is",inch)
# else:
#   inch = int(input("How many inches?"))
#   cm = inch * 2.5
#   print("In cms, it is",cm)


# Did student pass or fail?
# quiz = int(input("Please enter your quiz grade: "))
# midterm = int(input("Please enter your midterm grade: "))
# final = int(input("Please enter your final grade: "))
# total_grades = quiz + midterm + final
# if total_grades < 60:
#   print("You have failed the class")
#   print("You need to retake the class")
# else:
#   print("You have passed the class")
#   print("Congratulations")


#calculate the salary of the an employee
# salary = 500
# number_of_kids = int(input("How many kids do you have? "))
# if number_of_kids > 0:
#   salary = salary + number_of_kids * 50
# print("Your salary is: ",salary)

# Did the student pass the class?
# quiz = int(input("Please enter your quiz grade: "))
# midterm = int(input("Please enter your midterm grade: "))
# final = int(input("Please enter your final grade: "))
# total_grades = quiz + midterm + final
# if total_grades < 60:
#   print("You have failed the class")
#   print("You must retake the class")


#wear a jacket if the weather is cold
# temp = int(input("What's the temp outside: "))
# if temp < 10:
#   print("You should wear a jacket outside")
