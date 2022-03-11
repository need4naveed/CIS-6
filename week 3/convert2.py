#A program to convert Fahrenheit temps to Celsius 

def main ():
    print("This program convert temps from Fahrenheit to Celsius")
    fahrenheit = eval(input("What is the Fahrenheit temperature? "))
    celsius = 5/9 * (fahrenheit - 32)
    print("The temperature is", celsius, "degrees celsius.") 
main()
