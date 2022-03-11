#Program determines the sum of the cubes of n natural numbers

def main():
    print("Program determines the sum of the cubes of n natural numbers")
    natnum = eval(input("How many natural numbers do you want to add: "))
    add = 0
    for i in range (natnum + 1):
        add = add + i ** 3
    print(add)

main()
