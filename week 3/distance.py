#program to determine the distance between 2 points
import math

def main():
    print("This program determines the distance between 2 points.")
    print()
    
    px1, py1 = eval(input("Input the first point in x, y format: "))
    px2, py2 = eval(input("Input the second point in x, y format: "))
    slopey = py2 - py1
    slopex = px2 - px1
    print("The slope is", slopey, '/', slopex)
    dis = math.sqrt(slopex + slopey)
    print("The distance between the points is", dis)

main()
