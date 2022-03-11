# A program to calculate the total bill after taxes and tip

def getBill(bill,tax,tip):
    total = bill + (bill * tax) + (bill * tip)
    print("Your final bill is:", total)

def getTax(bill,tax):
    taxes = bill * tax
    print("Taxes paid:", taxes)

def getTip(bill,tip):
    tips = bill * tip
    print("Amount tipped:", tips)

def main() :
    print("This program calculates the total bill after taxes")
    bill = eval(input("Enter the initial bill amount: "))
    tax = eval(input("Enter the sales tax % as a decimal: "))
    tip = eval(input("Enter the tip % as a decimal: "))
    print()
    getBill(bill,tax,tip)
    getTax(bill,tax)
    getTip(bill,tip)
    
main()
    
