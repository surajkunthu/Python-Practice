############################################################################
# Suraj Kunthu
# This project will build a phone number from digits entered by the user
# June 19, 2019
############################################################################

#Establish that numPhone is a string variable
numPhone = ''
#Initialize counter
counter = 0

#Create limit for 10 digits in a phone number
while counter < 10:
    #Ask user to enter a digit from 0-9
    digit = int(input("Enter a digit (0-9): "))
    #Only if the digit is inbetween 0 and 9, the input will be used
    if digit >= 0 and digit <= 9:
        #Replace previous numPhone value with new value + the new string input
        numPhone = numPhone + str(digit)
        #Increment the steps
        counter = counter + 1

#Assign numPhone to proper phone number formatting
numPhone = "(" + numPhone[0:3] + ")" + numPhone[3:6] + "-" + numPhone[6:10]

#Display phone number
print('\n')
print(numPhone)
