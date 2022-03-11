#Finds if n is a prime number
import math

num = int(input("Enter number of primes: "))
primes = [2, 3]

def is_prime(n):
    for i in range(2, int(math.sqrt(n)+ 1)): 
        if (n % i) == 0: #if number evenly divides then it's not a prime
            return False
        else:
            return True

if num > 2:
    for i in range (2, num + 1):
        if is_prime(i) == True: #add number to list if prime
            print(i)
            primes.append(i)    
    print("Here are prime numbers up to", num,"\n", primes)
 
else:
    print("Enter an integer greater than 2")


