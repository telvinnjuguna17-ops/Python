# Gross salary in variable
Salary = float(input("Enter Gross Salary:"))
if Salary <= 5999 :
    print("Contribution is:Ksh 150.00")

elif Salary >=6000  and Salary <=7999 :
    print("Contribution is:Ksh 300.00")  

elif Salary >=8000 and Salary <=11999 :
    print  ("Contribution is:Ksh 400.00")  

elif Salary >=12000 and Salary <= 14999 :
    print ("Contribution is:Ksh 500.00")

elif Salary >=15000 and Salary <= 19999:
    print ("Contribution is:Ksh 600.00")

elif Salary >= 20000 and Salary <= 24999:
    print ("Contribution is:Ksh 750.00")

elif Salary >= 25000 and Salary <= 29999:
    print ("Contribution is:Ksh 850.00")  

elif Salary >=30000 and Salary <= 49999:
    print ("Contribution is:Ksh 1,000.00")  

elif Salary >= 50000 and Salary <= 99999:
    print ("Contribution is:Ksh 1,500.00")

else:
    print ("Contribution is:Ksh 2,000.00")
                             