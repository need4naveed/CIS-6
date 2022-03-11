#Program determines the nth number in the Fibonacci sequence

def fib(n): 
    if n==0: 
        return 0
    elif n==1: 
        return 1
    else: 
        return fib(n-1) + fib(n-2) 

def main():
    print("This program finds the nth number in the Fibonacci sequence")
    n = eval(input("What number do you want to find: "))
    print("The answer is: ", fib(n))

main()
