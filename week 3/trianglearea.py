import math

def main():
    print("Program to calculate the area of a triangle.")
    print("")
    a, b, c = eval(input("Enter the length of each side seperated by commas: "))
    s = (a + b + c)/2
    area = math.sqrt(s *(s - a)*(s - b)*(s - c))
    print("The area of the triangle is ", area)

main()
