from random import *

def main():
    printIntro()
    probA, probB, n = getInputs()
    matchA, matchB = simNGames(n, probA, probB)
    printSummary(matchA, matchB)

def printIntro():
    print("This program simulates a game of racquetball between two")
    print('players called "A" and "B". The abilities of each player is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("reflects the likelihood of a player winning the serve.")
    print("Player A has the first serve.")

def getInputs():
    a = eval(input("What is the prob. player A wins a serve? "))
    b = eval(input("What is the prob. player B wins a serve? "))
    n = eval(input("How many games to simulate? "))
    return a, b, n

def simNGames(n, probA, probB):
    winsA = 0
    winsB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB


def simOneGame(probA, probB):
    scoreA = 0
    scoreB = 0
    x = 1
    serving = altServe(x) #implements function to pick server
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"
    x = x + 1 #adjust x value for next serve
    return scoreA, scoreB

def gameOver(a,b):
    return a == 15 or b == 15

def altServe(x): #function to alternate even and odd serves
    if x % 2 == 0:
        return "A"
    else:
        return "B"

def printSummary(winsA, winsB):
    n = winsA + winsB
    print ("\nGames simulated:", n)
    print ("Wins for A: {0} ({1:0.1%})".format(winsA, winsA/n))
    print ("Wins for B: {0} ({1:0.1%})".format(winsB, winsB/n))

main()
