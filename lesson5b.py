# Functions with parameters
# They are values that get passed as arguments given to a function inside of the parenthesis.

def greeting(name):
    print(f"{name} How are you?Hope everything is fine.")

greeting("Telvin")
greeting("Liana")


print("====================")
def message(name):
    print(f"Hello {name}.We shall be having a general meeting on date.....please avail youself.")
    
message("Joy")
message("Alvin")

# Create a function that accepts parameters to add two numbers
def addition (x,y):
    sum = x + y
    print("The sum of the numbers is:",sum)
addition(45 , 65)
addition(78 , 92)