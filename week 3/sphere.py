import math

def main():
    print("This program will calculate the volume and surface")
    print("area of a sphere given it's radius.")

    r = eval(input("\nEnter the radius: "))

    v = (4 / 3) * math.pi * r ** 3
    print("\nThe volume of the sphere is: ", v)
    
    a = 4 * math.pi * r ** 2
    print("The surface area of the sphere is: ", a)

main()
