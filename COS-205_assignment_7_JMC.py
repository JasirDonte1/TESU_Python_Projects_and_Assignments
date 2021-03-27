

def main():

    print("Enter two positive integers")
    print("Enter the first number")
    x = int(input())
    while (x < 1):
        print("Integers must be positive! \nEnter two positive integers")
        x = int(input())

    print("Enter the second number")
    y = int(input())

    while (y < 1):
        print("Integers must be positive! \nEnter two positive integers")
        y = int(input())
        
        
    
    if(x==y):
        print("GCD = ", x)
        print("Do you want to compute two different numbers? (Y/N)")
        answer = input()

        
    elif (x > y):
        largest = x
        smallest = y
        z = gcd(x, y)
        print("GCD = ", z)
        print("Do you want to compute two different numbers? (Y/N)")
        answer = input()
              
    else:
        largest = y
        smallest = x
        z = gcd(x, y)
        print("GCD =", z)
        print("Do you want to compute two different numbers? (Y/N)")
        answer = input()
        
    toRecurse(answer)   


def toRecurse(ans):

 
    if (ans == "No" or "N"):
        quit()
        
    if (ans == "Yes" or "Y"):
        main()
    

def gcd(x, y):
    
  while(y):     
    x, y = y, x % y    #n, m=m, n%m 
    
  return x



#driver starts here

main()
