#tuples
cars = ('cadillac','chevrolet','ford')

#lists
names = ['basma','khalid','yousef','hani', 'jassim', 'sarah']
numbers = [1,15,26,18,24,91,71,18]

#mathematical operations
# print("Max = ",max(numbers))
# print("Min = ",min(numbers))
# print("Sum = ",sum(numbers))
# print("average = ",sum(numbers)/len(numbers))

#sort a list
# names.sort()
# print(names)

#delete an item at a specific poisition
# for x in range(3):
#   location_to_remove = int(input("What location?"))
#   del names[location_to_remove]
#   print(names)

#delete an item from a list
# name_to_remove = input("What name?")
# names.remove(name_to_remove)
# print(names)

#insert at a specific location
# for x in range(3):
#   name_to_add = input("What name?")
#   location_to_add = int(input("What location?"))
#   names.insert(location_to_add,name_to_add)
#   print("Just added ",name_to_add)
#   print(names)
#   print("\n")

#add an item to the end of the list
# for x in range(3):
#   name_to_add = input("What name?")
#   names.append(name_to_add)
#   print("Just added ",name_to_add)
#   print(names)

#search for the location of an item
# searched_name = input("What name?")
# name_index = names.index(searched_name)
# print("Found it at index = ",name_index)

#to search for an item in a list
# searched_name = input("What name?")
# if searched_name in names:
#   print("Yep... Found it")
# else:
#   print("Sorry.. the name isn't there")

#protect from error if index is too hight
# get_index = int(input("Please enter index:"))
# if get_index < len(names):
#   print("the name is",names[get_index])
# else:
#   print("Your index was tooooo high")

#length of a list - or the number of items in a list
#print("Total items = ",len(names))

#printing an index
# for x in range(3):
#   get_index = int(input("Please enter index:"))
#   print("the name is",names[get_index])

# location = 3
# print("At index 3, the item is",names[3])


#printing the full list at once
#print(names)

#printing a list
#for a_name in names:
#  print("Name =",a_name)

#printing letters
# name = "Sulaiman Ali"

# for letter in name:
#   print("= ",letter)
