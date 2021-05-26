#calculate salaries
enter_new_emp = "y"
total_managers = 0
total_employees = 0
total_salaries = 0
while(enter_new_emp == "y"):
  salary = 0
  num_kids = int(input("\nEnter number of kids:"))
  job = int(input("Enter job, 1-manager, 2-employee:"))
  
  if job == 1:
    salary = 1000
    total_managers = total_managers + 1
  else:
    salary = 500
    total_employees = total_employees + 1  
   
  salary = salary + 50*num_kids
  total_salaries = total_salaries + salary
  print("Your salary is:",salary)
  enter_new_emp = input("\nWant to input more (y/n)")

print("\n\nTotal managers = ",total_managers)
print("Total employees = ",total_employees)
print("Average salary = ",total_salaries/(total_employees+total_managers))

#multiply numbers together
total_multi = 1
cont = "y"
while (cont == "y"):
  new_num = int(input("What's the number:"))
  total_multi = total_multi * new_num
  print("You just added",new_num,"to the numbers\n")
  cont = input("want to enter a number? (y/n)")

print("\nThe total multiplication = ", total_multi)

while (input("want to enter a number? (y/n)") == "y"):
  new_num = int(input("What's the number:"))
  total_multi = total_multi * new_num
  print("You just added",new_num,"to the numbers\n")

print("\nThe total multiplication = ", total_multi)



#find the oldest person
ages = [12, 16, 9, 5, 68, 45, 64, 26, 87 ,8]
maximum_age = 0
for age in ages:
  if age > maximum_age:
    maximum_age = age
    print("----- found a new older person, where their age is:",age)
  print("currently, oldest person is",maximum_age,"years old\n")

print("\nThe oldest person is",maximum_age,"years old")

#find youngest person
min_age = 200
for age in ages:
  if age < min_age:
    min_age = age

print("\nThe youngest person is",min_age,"years old")


#find if your list of cities contain a specific city
cities = ["Salmiya","Hawally", "Mishref", "Abdullah almubarak", "AlQusoor", "Kaifan"]

city_search = input("Please enter the city name:")

search_result = "Did not find the city"

for city in cities:
  if city == city_search:
    search_result = "Found the city"

print(search_result)

#add numbers inside a list
numbers = [12.5, 16.9, 9.8, 5.8, 68.7,45, 98, 98,87 ,8]
total = 0

for number in numbers:
  total = total + number
  print("So far, the total is: ", total)
  
print("\n\nThe total = ", total)

#convert a list of lengths in inches to cm
lengths_inch = [5, 9, 11, 5, 4.5, 8, 89, 11, 22]

for length in lengths_inch:
  print("We are converting ", length, " to cm.")
  print("The length is cm = ",length * 2.5)
  print("\n")
