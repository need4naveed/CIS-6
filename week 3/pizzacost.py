#program to determine cost per square inch of pizza given price and diameter
import math

def main():
    print("Program to determine cost per square inch of pizza")
    cost = eval(input("How much did the pizza cost: "))
    d = eval(input("What is the diameter of the pizza in inches: "))
    a = math.pi * (d/2) ** 2
    inchprice = a / cost
    print("The pizza cost ",inchprice, "per square inch")

main()
