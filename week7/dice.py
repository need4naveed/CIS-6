#Two player dice game. Asks players for max score and bad luck number.
#Rolling bad luck will subtract from your score instead of adding.

import random

roll = ""
player1 = 0
player2 = 0

def dieroll(): #function for rolling die
    print("Rolling dice...")
    die = random.randint(1,6)
    print("You rolled:", die)
    return die

print("This is a two player dice rolling game.") #intro to game
print("Take turns rolling to gain score.")
print("If you roll unlucky it will subtract your score.")
smax = eval(input("What is the max score for this game: ")) #set max 
bluck = eval(input("What is the bad luck number: ")) #set bad luck number


while player1 < smax and player2 < smax: #Plays until someone reaches max score
    print("")
    print("Player 1 score:", player1)
    print("Player 2 score:", player2)
    roll = input("Player 1 roll? Y/N: ").lower()
    if roll == "y":
            temproll = dieroll() #sets die roll to temp variable
            if temproll == bluck: #checks for badluck number then + or - score
                player1 -= temproll
            else:
                player1 += temproll
                       
    roll = input("Player 2 roll? Y/N: ").lower()
    if roll == "y":
            temproll = dieroll()
            if temproll == bluck:
                player2 -= temproll
            else:
                player2 += temproll
        
    
if player1 >= smax: #Congratulations message
    print("Congrats player 1! Final score:", player1)
elif player2 >= smax:
    print("Congrats player 2! Final score:", player2)
