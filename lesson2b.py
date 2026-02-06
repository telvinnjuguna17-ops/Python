# Tuple 
# A tuple is an immutable type of a list (It cannot change)
# To introduce a tuple , we use the parethensis ()

counties = ("Nairobi", "Mombasa","Nakuru", "Eldoret","Kajiado","Kisii")
print(counties)
print(type(counties))

# Slicing of tuples
print(counties[3:])

# Accessing items of a tuple by use of the indexes
print(counties[5])

# Note : Below will generate an error
# attribute error
counties.append("Machakos")
print(counties)