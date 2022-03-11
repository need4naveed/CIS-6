#A program to determine price of a coffee order given shipping and per pound cost

def main():
    print("This program calculates the cost of a coffee order.")
    print()
    pounds = eval(input("How many pounds of coffee are in the order: "))
    cost = ((10.50 + .86) * pounds) + 1.50
    print("The total total cost of the order is", cost)

main()
