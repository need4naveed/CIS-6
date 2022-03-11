#Number guessing game. Asks for number range and allows user to guess the number.
#User can quit by entering -1 as a guess, and can replay the game multiple times.

import random


def guessgame():
    print("Number guessing game. Enter '-1' as a guess to quit.")
    smin,smax = eval(input("Enter the range of numbers seperated by comma: "))
    print("Generating number...")
    rando = random.randint(smin,smax) #random number assigned between min and max
    guess = rando + 1 #reassign guess to not match random number
    while guess != rando: #loops until user guesses correctly
        guess = eval(input("What is your guess: "))
        gcheck(guess,rando)
        if guess == -1: #quits if user enters -1
            break
    game = input("Play again? Y/N: ").lower() 
    if game == "y": guessgame() #entering y will restart the game

def gcheck(g,r): #function for checking guess
    if g > r:
        print("Guess too high")
    elif g < r:
        print("Guess too low")
    elif g == r:
        print("Wow you're so smart, you got it!")
    
guessgame() #plays game when program is opened
