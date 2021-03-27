


def squareEach(nums):
    counter = 0
    for x in nums:
        nums[counter] = nums[counter]*nums[counter]
        counter = counter + 1
        
    return nums
        
        
    
def sumList(nums):

    sumOfList = 0
    counter = 0
    for x in nums:
        sumOfList = sumOfList + nums[counter]
        counter = counter + 1
        
    return sumOfList

    
def toNumbers(strList):
    counter = 0
    for x in strList:
        strList[counter] = int(strList[counter])
        counter = counter + 1

    return strList

def sumOfSquares():
    file_name = input("Enter file name: ")  #must enter full path to file 
    file = open(file_name,"r")  
    file_single_line = file.readlines()
    count = 0
    array = []
    for x in file_single_line:
        array = x.split(" ")

    sumOfSquares = sumList(squareEach(toNumbers(array)))
        
        
    print ("Sum of squares in list =",sumOfSquares)
    
    



sumOfSquares()






