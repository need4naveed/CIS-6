#A program to convert Celsius temps to Fahrenheit 

def main ():
    print("This program shows temperature from Celsius to Fahrenheit in increments of 10 from 0 to 100")
    celsius = 0
    for i in range(11):
        fahrenheit = 9/5 * celsius + 32
        print(celsius, fahrenheit)
        celsius = celsius + 10
main()
