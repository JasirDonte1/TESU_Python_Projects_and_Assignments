def main():
    print('Enter the radius: ')
    user_input = input()
    radius = int(user_input)           
    area = sphereArea(radius)
    volume = sphereVolume(radius)
    print('Area = ', area)
    print('Volume =', volume)
    

def sphereArea(radius):
    r = radius * radius
    pi = 3.14159265359
    return 4*r*pi
    
def sphereVolume(radius):
    pi = 3.14159265359
    r = radius * radius * radius 
    return (4/3)*pi*r


main()
