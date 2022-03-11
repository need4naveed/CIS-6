#Program determines the nth number in the Fibonacci sequence

def main():
    print("This program finds the nth number in the Fibonacci sequence")
    num = eval(input("What number in the sequence do you want to find: "))
    for i in range (num):
        (i + (i - 1))
    print(i)
    print("The answer is: ", fib(num))

def fib(n): 
    if n==0: 
        return 0
    elif n==1: 
        return 1
    else: 
        return fib(n-1) + fib(n-2) 

main()
