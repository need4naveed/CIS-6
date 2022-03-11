#This program calculates the nth number of the fibonacci sequence
#and keeps count of how many times the fib function is called

class FibCounter():
    def __init__(self): 
        self.count = 0 #Initialize count variable and sets to 0
    def getCount(self):
        return self.count #returns the fib count
    def fib(self,n): #recursive fib function for nth number in sequence
        self.count += 1 #adds 1 to count variable each call
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n-1) + self.fib(n-2)
    def resetCount(self): #dont even need this but the book told me to put it
        self.count = 0

print('This program calculates the nth number of the fibonacci sequence\n')
def main():
    n = int(input('What number would you like to calculate (-1 to end): '))
    if n != -1: #allows the user to input -1 to end
        fibn = FibCounter() #creates a new FibCounter variable to call
        print('fib(' + str(n) + ') is', fibn.fib(n), 'and took', fibn.getCount(), 'calls.')   
        main()
main()
