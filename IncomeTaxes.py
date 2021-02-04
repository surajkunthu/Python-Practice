############################################################################
# Suraj Kunthu
# This project calculates the income taxes an individual will have to pay based on their filing status and income.
# June 12, 2019
############################################################################

#Ask the user for their filing status
filingStatus = str(input("Enter your tax status (Single or Married Filing Jointly): "))

#Ask the user for their annual income
income = int(input("Enter your income: "))

#First, determine filing status
#Second, determine what tax amount will be based on user inputted income
#Third, calculate tax
#Final, display user's tax amount
if(filingStatus == 'Single'):
    if (income > 510300):
        tax = income * 0.37
    elif (income <= 510300 and income > 204101):
        tax = income * 0.35
    elif (income < 204100 and income > 160726):
        tax = income * 0.32
    elif (income < 160725 and income > 84201):
        tax = income * 0.24
    elif (income < 84200 and income > 39476):
        tax = income * 0.22
    elif (income < 39475 and income >= 9700):
        tax = income * 0.12
    else:
        tax = income * 0.10
    print('\n')
    print("Your tax amount is", '${:.2f}'.format(tax))
    
elif(filingStatus == 'Married Filing Jointly'):
    if (income > 612350):
        tax = income * 0.37
    elif (income <= 612350 and income > 408201):
        tax = income * 0.35
    elif (income < 408200 and income > 321451):
        tax = income * 0.32
    elif (income < 321450 and income > 168401):
        tax = income * 0.24
    elif (income < 168400 and income > 78951):
        tax = income * 0.22
    elif (income < 78950 and income >= 19401):
        tax = income * 0.12
    else:
        tax = income * 0.10
    print('\n')
    print("Your tax amount is", '${:.2f}'.format(tax))
    
else:
    print('\n')
    print("Invalid entry")

