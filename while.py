number_failed = 0
number_passed = 0
new_grade = "y"
while new_grade == "y":
  student_final_point = int(input("Enter grade: "))
  if student_final_point >= 60:
    number_passed = number_passed +1
  else:
    number_failed = number_failed + 1
  new_grade = input("\nAnother grade?")
    
print("Passed: ", number_passed)
print("Failed: ",number_failed)

# Add numbers
# total = 0
# new_number = int(input("Enter number (0 to finish):"))
# while new_number > 0:
#   total = total + new_number
#   print("Total so far = ",total)
#   new_number = int(input("\nEnter number (0 to finish):"))

# print("The total = ", total)

# #adding two numbers
# continue_adding = "y"
# while continue_adding == "y":
#   num1 = int(input("Enter first number:"))
#   num2 = int(input("Enter second number:"))
#   print("the addition is: ", num1+num2)
#   continue_adding = input("Want to add more?")

# print("Thank you for using the calculator")

#Lists
# names = ["Ahmed", "Khalid", "Yousef"]
# ages = [15,19,23,29,27,28,16,18,17]
# anything = [78, "A", 98.2, 44.322, "Ahmed", 75]

# for name in names:
#   print(name)  

# for age in ages:
#   print("Your age is: ",age)
#   print("You were born in ", 2021-age)
