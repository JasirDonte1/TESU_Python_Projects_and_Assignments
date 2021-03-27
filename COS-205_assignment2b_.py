
def factorialFinder(n):
    counter = n
    x = 0
    while(n > 0):
        x = n + x
        n = n - 1

    return x 
        


n = float (input("Enter value of n "))

print(factorialFinder(n))

