

#*********Find number in base***************
"""""
Two integers (x and b) as inputs and returns a string that represents the number x    
 in base b 
"""
import math
x = int(input("Enter a number to calculate in base the next number: "))
b = int(input("Enter the base you want to calculate: "))
answer = math.log(x,b)
print (answer)