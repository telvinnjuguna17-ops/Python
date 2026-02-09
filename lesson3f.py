# # create a python program that is able to determine whether a number entered is an odd number or an even number
# number = int(input("Enter your number here."))
# if number % 2 == 0 :
#     print("the number is even")
# else:
#     print("the number is odd")    

# create a python program that is able to determine whether a person can donate blood based on the age and weight of the person.If the weight is greater than 50kg and age is above 18 years ,then the person can donate , else not possible

age =float(input("Enter age:"))
weight = float(input("Enter weight here:"))

if age >= 18 and weight > 50:
    print("Can donate")
else:
    print("not Possible")       