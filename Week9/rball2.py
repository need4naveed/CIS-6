from random import random

def main():
    printIntro()
    probA, probB, n = getInputs()
    matchA, matchB = simNMatches(n, probA, probB)
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

def simNMatches(n, probA, probB):
    matchA = 0
    matchB = 0
    for i in range(n):
        winsA, winsB = simOneMatch(probA, probB)
        if winsA > winsB:
            matchA = matchA + 1
        else:
            matchB = matchB + 1
    return matchA, matchB

def simOneMatch(probA, probB):
    winsA = 0
    winsB = 0
    x = 1
    while winsA !=2 and winsB !=2:
        scoreA, scoreB = simOneGame(probA, probB, x)
        if scoreA > scoreB:
            winsA = winsA + 1
            x = x+1
        else:
            winsB = winsB + 1
            x = x+1
    return winsA, winsB

def simOneGame(probA, probB, x):
    serving = altServe(x)
    scoreA = 0
    scoreB = 0
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                serving = "B"
        elif serving == "B":
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"
    return scoreA, scoreB

def altServe(x):
    if x % 2 == 0:
        return "A"
    else:
        return "B"

def gameOver(a, b):
    if a == 0 and b == 7:
        return b == 7
    elif b == 0 and a == 7:
        return a == 7
    elif abs(a-b) >= 2:
        return True
    else:
        return False

def printSummary(matchA, matchB):
    # Prints a summary of wins for each players
    n = matchA + matchB
    print("\nGames simulated: ", n)
    print("Wins for A: {0} ({1:0.1%})".format(matchA, matchA/n))
    print("Wins for B: {0} ({1:0.1%})".format(matchB, matchB/n))

main()
