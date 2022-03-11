from math import pi

def sa(r):
    return 4 * pi * r * r
    
def vol(r):
    return (4 / 3) * pi * r * r * r

def main():
    print("This program will calculate the volume and surface")
    print("of a sphere given it's radius.")
    print("")
    radius = eval(input('Please Enter the Radius of a Sphere: '))
    print("The surface area is: ", sa(radius))
    print("The volume is: ", vol(radius))

main()

