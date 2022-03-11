# A program to compute the value of an investment

def main() :
    print("This program calculates the future value of investments")
    invest = eval(input("Enter the yearly investment amount: "))
    apr = eval(input("Enter the annual interest rate: "))
    years = eval(input("Enter the number of years for investment: "))
    total = 0
    for i in range(years) :
        total = invest + (total * (1 + apr))
    print ("The value in", years, "years is: ", total)
main()
