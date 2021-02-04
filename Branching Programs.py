# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#x = int(input('Enter an integer: '))

#if x%2 == 0:
#    print('')
#    print('Even')
#else:
#    print('')
#    print('Odd')
# print('Done with conditional')
    
# Nested Conditionals
    
#if x%2 == 0:
#    if x%3 == 0:
#        print('Divisible by 2 and 3')
#    else:
#        print('Divisible by 2 and not by 3')
#elif x%3 == 0:
#        print('Divisible by 3 and not by 2')
#print('Done with Conditional')

x = float(input("Enter a number for x:  "))
y = float(input("Enter a number for y:  "))
if x == y:
    print("x and y are equal")
    if y != 0:
        print("therefore , x/y is ", x/y)
elif x < y:
    print('')
    print("x is smaller")
else:
    print('')
    print("y is smaller")
print('')    
print("Thanks!")
    
