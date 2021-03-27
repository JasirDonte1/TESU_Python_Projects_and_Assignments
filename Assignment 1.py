

#prompts for user input
initial = float(input("Enter initial amount "))
rate = float(input("Enter interest rate "))
periods = int(input("Enter number of periods in a year "))
duration = int(input("Enter the number of years of duration "))

multiplier = rate/periods 
count = duration*periods

#loop calculates value
while count > 0:
    temp = initial*multiplier 
    initial = initial+temp
    count = count - 1
    
#round is used to store same value to the second decimal place
initial = round(initial,2)
print(initial)
