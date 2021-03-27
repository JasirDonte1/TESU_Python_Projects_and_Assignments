

#user inputs 
initial = float(input("Enter initial amount "))
rate = float(input("Enter interest rate "))
periods = int(input("Enter number of periods in a year "))
duration = int(input("Enter the number of years of duration "))

multiplier = rate/periods 
count = duration*periods

while count > 0:
    temp = initial*multiplier 
    initial = initial+temp
    count = count - 1
    
initial = round(initial,2)
print(initial)
