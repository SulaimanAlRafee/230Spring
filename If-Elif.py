#largest of 3 numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 > num2 and num1 > num3:
  print("largest number is:", num1)
elif num2 > num1 and num2 > num3:
  print("largest number is:", num2)
else:
  print("largest number is:", num3)


#orders - different way
# number_of_pizzas = 0
# PRICE_OF_PIZZA = 3.2
# number_of_hamburgers = 0
# PRICE_OF_HAMBURGER = 1.5
# number_of_drinks = 0
# PRICE_OF_DRINK = .7

# number_of_pizzas = float(input("How many pizzas do you want?"))
# number_of_hamburgers = float(input("How many hamburgers do you want?"))
# number_of_drinks = float(input("How many drinks do you want?"))

# total_price = number_of_pizzas * PRICE_OF_PIZZA \
#               + number_of_hamburgers * PRICE_OF_HAMBURGER \
#               + number_of_drinks * PRICE_OF_DRINK

# print("Your total price is: ",total_price)

#Cost of meal in a restaurant
# pizza_order = input("Do you want pizza? (yn)")
# number_of_pizzas = 0
# PRICE_OF_PIZZA = 2.8
# if pizza_order == "y":
#   number_of_pizzas = int(input("How many pizzas do you want?"))
# price_of_pizzas = number_of_pizzas * PRICE_OF_PIZZA

# hamburger_order = input("Do you want a hamburger? (yn)")
# number_of_hamburgers = 0
# PRICE_OF_HAMBURGER = 1.5
# if hamburger_order == "y":
#   number_of_hamburgers = int(input("How many hamburgers do you want?"))
# price_of_hamburgers = number_of_hamburgers * PRICE_OF_HAMBURGER

# drink_order = input("Do you want drinks? (yn)")
# number_of_drinks = 0
# PRICE_OF_DRINK = .7
# if drink_order == "y":
#   number_of_drinks = int(input("How many drinks do you want?"))
# price_of_drinks = number_of_drinks * PRICE_OF_DRINK

# total_price = price_of_pizzas + price_of_hamburgers + price_of_drinks
# print("Your total price is: ",total_price)


#calculate salary of employee
# salary = 500
# print("m = married, d = divorced, s = single, w = widowed")
# marital_status = input("What is your marital status?")

# if marital_status == 'm':
#   salary = salary + 100
# elif marital_status == 'd' or marital_status == 'w':
#   salary = salary + 50

# number_of_kids = int(input("How many children do you have?"))
# salary = salary + number_of_kids * 50

# print("Your salary is", salary)

#conversion of lengths
# print("Please select one of the following:")
# print("    convert from cm to in")
# print("    convert from in to cm")
# result = input("Please select cm or in: ")
# if result == "cm":
#   cm = int(input("How many cm?"))
#   inch = cm / 2.5
#   print("In inches, it is",inch)
# elif result == 'in':
#   inch = int(input("How many inches?"))
#   cm = inch * 2.5
#   print("In cms, it is",cm)
# else:
#   print("You must write either in or cm")

#Student letter grade
# grade = int(input("What's your total grade: "))
# if grade >= 90:
#   print("Your letter grade is an A")
# elif grade >= 80 and grade < 90:
#   print("Your letter grade is an B") 
# elif grade >= 70 and grade < 80:
#   print("Your letter grade is an C")
# elif grade >= 60 and grade < 70:
#   print("Your letter grade is an D") 
# elif grade < 60:
#   print("Your letter grade is an F") 
# else:
#   print("YOU ARE HERE")

