# Python lists
# A list in python is a collection of the items that are ordered in a certain way .
# A list is introduced by the use of the square brackets [].
# The items of a list are stored inside of the indexes. Note : In programming we start counting from index Zero (0).bmw,benze,hiance, .....
# A list is mutable i.e the contents of a list can be changed.

cars = ["BMW", "Benze", "Hiance", "Prado", "Probox", "Range","Lambo"]
print(cars)
print(type(cars))

# Accessing the items  of a list 
print(cars[2]) 
print("The car on index four is: ", cars[4])

# List slicing- Thi is creating  a list from a given bigger list
print(cars[4:])

# Printing from index 0to3 
print(cars[0:4])

# Printing from Hiance to probox
print(cars[2:5])

# List mutability
# We use the function append to add an item at the end of a list
cars.append("Mercedes")
print(cars)

cars.append("Subaru")
print(cars)

# We use the pop function to remove an item at the end of the list
cars.pop()
print(cars) 

# we can use an index to add items on a list
cars[5] = "Pajero"
print(cars)

# We  can use the sort function to sort out items in alphabetical order
cars. sort()
print(cars)