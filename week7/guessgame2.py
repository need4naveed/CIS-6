#Number guessing program that will ask the user for the range and 6 numbers
#and guess each of their numbers.
import random

def guessgame():
    print("This program will try to guess your 6 numbers in a given range.")
    smin,smax = eval(input("Enter the range for the numbers seperated by comma: "))
    answers = []
    rando = []  
    for i in range(6):
        answers.append(eval(input("Enter a number for the computer to guess: ")))
    print(answers)
    for n in answers:
        guess = random.randint(smin,smax)
        print("My guess is: ",guess)
        rando.append(gcheck(guess,n,smin,smax))
    print("Your numbers are: ", rando)


def gcheck(g,n,smin,smax): #continues guessing each number until it guesses correctly
    while True:
        if g > n: #if the guess is higher than the number than the upper bound is set to the guess
            smax = g
            print("Darn,",g,"was too high")
            g = random.randint(smin,smax)
            print("My guess is: ",g)
        elif g < n: #if the guess is low than the number than the lower bound is set to the guess
            smin = g
            print("Darn,",g,"was too low")
            g = random.randint(smin,smax) 
            print("My guess is: ",g)
        elif g == n: #if the guess is correct it returns that value
            print("Got that one!")
            return g
        
        
        
            
    
    
guessgame()
