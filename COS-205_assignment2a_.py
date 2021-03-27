import math

#function will return the area of a triangle 
def calculateArea(a,b,c):
    s = (a+b+c)/2
    
    x = s-a
    y = s-b
    z = s-c

    A = math.sqrt(s*x*y*z)
    
    return A


#prompts user for input 
a = float (input("Enter the three sides of a triangle\nEnter side 1 "))
b = float (input("Enter side 2 "))
c = float (input("Enter side 3 "))

print(calculateArea(a,b,c))
