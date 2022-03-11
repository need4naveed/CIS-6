#Finds if n is a prime number

num = eval(input("number: "))
if num > 2:
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
 
else:
    print("Enter an integer greater than 2")

