#Program determines the sum and cube of sum of n natural numbers

def sumN(n):
    add = 0
    nnum = n
    for i in range (n + 1):
        add = add + i
    print("The sum of", nnum, "natural numbers is:", add)

def sumNcubes(n):
    add = 0
    nnum = n
    for i in range (n + 1):
        add = add + i ** 3
    print("The sum of the cube of", nnum, "natural numbers is:", add)

def main():
    print("Program determines the sum and cube of sum of n natural numbers")
    n = eval(input("How many natural numbers do you want to add: "))
    sumN(n)
    sumNcubes(n)

main()
