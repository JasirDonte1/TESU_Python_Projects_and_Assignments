def main():
    print('Enter a number')
    n = int(input())
    a = 1
    b = 1
    if n > 2:
        while 2 < n:
            sequence = a + b
            b = sequence
            a = b - a
            n = n - 1
        print (sequence)
    else:
        print(1)



main()

        

