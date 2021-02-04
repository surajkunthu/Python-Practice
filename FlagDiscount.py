############################################################################
# Suraj Kunthu
# This program will calculate the price of the order of flags by multiplying
# the number of flags by the price, either discounted or original.
# July 08, 2019
############################################################################

# discount() is the function used to solve for the total discount put on the flags
def discount(n):
    # Formula for calculating discount
    discount = 4.50 * n
    # Return the value for discount
    return discount
 
# Main method - asks for number of flags
def main():
    # Initialize a value for n
    n = 1
    # Repeat program until user inputs "-1" to end loop
    while n != -1:
        
        # Ask the user for the number of flags, n
        n = eval(input("Enter a number of flags: "))

        # If user inputs 50 or more flags, price will be calculated with a discounted value
        if n >= 50:
            # Formula for total cost with discount
            totalCost = (20 * n) - discount(n)
            # Prints the total cost passed back from the function call discount()
            print("The total cost of the flags is:", '${:.2f}'.format(totalCost))
            
        # If user inputs "-1", loop will stop here and program will end
        elif n == -1:
            # Prints the user forced program end string
            print("Goodbye")
            
        # If user inputs less than 50 flags, price will be calculated normally
        else:
            # Formula for total cost without discount
            totalCost = (20 * n)
            # Prints the total cost passed back from the function call discount()
            print("The total cost of the flags is:", '${:.2f}'.format(totalCost))

# Call the main function
main()
