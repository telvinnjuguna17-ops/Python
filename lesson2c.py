# A dictionary is a data type that stores data in terms of key - value pair.
# it is introduced by the use of the curly braces {}
# the values stored inside of a dictionary can be of any data type .
# To access the values in the dictionary we use keys

phonebook = {
    "Lewis" : "25412345679" ,
    "Mary" : "25490777773" ,
    "Sreve" : "2547888888"
}
    # showing the entire dictionary
print(phonebook)
print(type(phonebook))

# Print out benson's number
print(phonebook["Sreve"])

print('===============')


player = {
    "name" : "Messi",
    "age" : 40,
    "teams" : ["PSG","Barcelona","Argentina"],
    "more" : {
        "children" : 3,
        "residence" : "US",
        "Phone" : (2543678899,2546678890,25467899000)
        }
}
# Print barcelona - the  second team he played for
print(player["teams"][1])

print("The second number of Messi is:",player["more"]["Phone"][1])