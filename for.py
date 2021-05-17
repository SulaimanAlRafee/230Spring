number_failed = 0
number_passed = 0
for student_grade in range(5):
  student_final_point = int(input("Enter points:"))
  if student_final_point >= 60:
    number_passed = number_passed +1
  else:
    number_failed = number_failed + 1
print("Passed: ", number_passed)
print("Failed: ",number_failed)


#add numbers up to
# total = 0
# for the_current_number in range(50):
#   total = total +  the_current_number
# print("The total is",total)

#Let's add 5 numbers together
# total = 0
# for repeat_addition in range(5):
#   current_num = int(input("Enter Number:"))
#   total = total + current_num
# print("The total is",total)

# for test in range(10):
#   print("\n==================")
#   print("the value is:",test)
#   print("the square is:",test*test)
#   print("==================\n")

# for x in range(10):
#   print("Hello there!")

# for x in range(5):
#   num1 = int(input("Enter number: "))
#   num2 = int(input("Enter number: "))
#   if num1 > num2:
#     print('The first number is larger.')
#   else:
#     print('The second number is larger.')

