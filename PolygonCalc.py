############################################################################
# Suraj Kunthu
# This project displays the area of a polygon from user given inputs for the...
# number of sides (n) and the length of each side (s)
# June 24, 2019
############################################################################

# Import math module
import math

# calcPolygon is the function used to solve for the area
def calcPolygon(n, s):

        # Formula used for solving the area
        calcPolygon = ((n * (s ** 2)/(4 * math.tan(((math.pi)/(n))))))
        
        # Return the value for calcPolygon
        return calcPolygon

# Main method - asks for two numbers to find calcPolygon
def main():
    
    # Ask the user for the number of sides of the polygon, n
    n = eval(input("Enter the number of sides of the polygon: "))

    # Ask user for the length of a side, s
    s = eval(input("Enter the length of a side: "))

    # Prints the area passed back from the function call calcPolygon,
    # passing in n and s formatted to 2 decimals
    print('\n')
    print("The area of the polygon is:", '{:.2f}'.format(calcPolygon(n, s)))

# Call the main function
main() 
