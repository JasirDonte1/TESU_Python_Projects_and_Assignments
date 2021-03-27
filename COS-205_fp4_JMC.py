

start = float(input("starting odometer reading is: "))

def getInfo():
    data = []
    counter = 0
    cancel = ""
    userInput = " "
    while (userInput != cancel):
        userInput = input("Enter current odometer reading and gas used with numbers seperated by as space. Press enter on a blank line when you are finished entering info (i.e. '60 3') ")
        if (userInput != ''):
            data.append(userInput)

    return data      #data is the array of input

def compute(data):
    gas = []
    odometer = []
    mpg = []        
    current = start #current odometer reading
    total_gas = 0
    counter = 0

    for x in data:        #split input into two different nums
        text = data[counter]
        toSplit = text.split()
        odometer.append(toSplit[0])
        gas.append(toSplit[1])
        counter = counter + 1
    legs = counter
    counter = 0
    for x in gas:     #calculate mpg for individual legs 
        total_gas = total_gas + float(gas[counter])
        rate = (float(odometer[counter])-current)/float(gas[counter])
        mpg.append(rate)
        current = float(odometer[counter])
        counter = counter + 1
    counter = 1
    
    for x in mpg:          #print mpg for each leg
        print("Leg", counter, "MPG =", mpg[counter-1])
        counter = counter + 1

    #calculate total mpg for trip 
    total_dist = current - start
    total_mpg = total_dist/total_gas
    
    
    print("Total MPG =", total_mpg)


compute(getInfo())
