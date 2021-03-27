
day = 29
month = 2
year = 2012

def leapYear():
    leapYear = False
    if (year%4 == 0):
            if(year%100 != 0):
                leapYear = True
    return leapYear

def verifyDate():
    
    validDate = False


    if (month == 1 or 3 or 5 or 7 or 8 or 10 or 12):
        if (day>0 and day<32):
            validDate = True
    if (month == 4 or 6 or 9 or 11):
        if (day>0 and day<31):
            validDate = True
    if (month == 2):
        if(leapYear() == True):
            if (day>0 and day<30):
                validDate = True
                    
        if (year%4 != 0):            
            if (day>0 and day<29):
                validDate = True
    

    return validDate


def computeDay():
    dayNum = 31*(month-1)+day
    if (month>2):
        dayNum = dayNum - ((4*month+23)//10)
        if (leapYear() == True):
            dayNum = dayNum+1
        
    return dayNum

def main():
    verified =  verifyDate()
    if (verified == False):
        print ("Date enter is not valid")
    else:
        day = computeDay()
        print("Computed day = ", day)

main()
