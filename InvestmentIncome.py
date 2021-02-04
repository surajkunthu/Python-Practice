############################################################################
# Suraj Kunthu
# This project displays the value of an investment after a given number of years at a given interest rate.
# June 01, 2019
############################################################################

#Ask the user for the initial investment amount, P
P = float(input("Enter the initial investment amount: "))

#Ask the user for the annual interest rate, r: 
r = float(input("Enter the annual interest rate: "))

#Ask the user for the number of years, t
t = float(input("Enter the number of years: "))

#Ask the user for the number of times the interest is compounded per year, n
n = float(input("Enter the number of times the interest is compounded per year: "))

#Compute new investment value by utilizing the following formula:
A = P * (1 + ((r)/(n)))**(n*t)

#Display new investment value
print ("\n")
print ("The investment value is:", '${:.2f}'.format(A))
