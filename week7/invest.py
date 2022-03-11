#program to calculate how long it would take an investment to double

def invest():
    rate = eval(input("Enter the annualized interest rate: "))
    year = 0
    principal = 1

    while principal < 2:
        interest = (principal * rate * year)
        principal = principal + interest
        year += 1
    print("The number of years it takes for your investment to double is",year)

invest()
