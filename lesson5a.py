# Python functions
# They are a block of code that performs a given task/action.They can be reused through out the program to perform different tasks.
# Functions are defined using the def keyword.(define)
# We have two main functions i.e:
#1In-built functions ->They come preinstalled with the interpreter i.e print(),Pop(),range(),Append() etc...
# 2. User defined functions =>They are created by a programmer to solve a particular task.
# To define a function you need to give it a name  followed by parenthesis
# For the functions , it is usually intentedand to invoke a function we use the function name.

def greetings():
    print("Hello,how are you?")

# Below we call the function by use of its name
greetings() 

print("====================")
# Addition function
def addition():
    num1 = 40
    num2 = 50
    sum = num1 + num2
    print("The sum of the numbers is :",sum)

addition()  

print("====================")
# Create a function that is able to multiply three values
def multiplication():
    num1 = 12
    num2 = 14
    num3 = 15
    multiplication = num1*num2*num3
    print("The Multiplication of the numbers is:",multiplication)

multiplication()  


print("====================")
# below is a division function
def divide():
    number1 = int(input("Enter the first number:"))
    number2 = int(input("Enter the second number:"))
    quotient = number1/number2
    print("The answer is:",quotient)
    print("----")

for function in range(3):
    divide()