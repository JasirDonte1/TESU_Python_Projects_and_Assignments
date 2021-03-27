def speedTicketCheck(speedLimit, clocked):
    fine = 50

    if (clocked > 89.9):
        
        fine = fine + 200
    
    toAdd = clocked - speedLimit
    toAdd = toAdd * 5

    fine = fine + toAdd

    print("Fine is:", fine)


def main():
    
    print("enter the speed limit")
    speedLimit = int(input())
    print("enter the clocked speed")
    clocked = int(input())

    if(speedLimit >= clocked):
        print("Speed was legal")
    else:
        print("Speed was illegal")
        speedTicketCheck(speedLimit, clocked)
        
        
        

main()
