
def main():
    file = open("/Users/JasirDonte/Documents/infile.txt","r")  
    file_single_line = file.readlines()
    count = 0
    array = []
    for x in file_single_line:
        data = x.split('\n')
        array.append(data[0])
    x = 1
    print("each # represents 1 apperance in file")
    while(x<11):
        print(x, ':', end =" ")
        for y in array:
            if (int(y) == x):
                print('#', end =" ")
        print("\n")
        x = x+1
        

main()

