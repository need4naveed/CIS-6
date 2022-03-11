#This program checks to find the largest number in a list

def maximum(xlist):
    if len(xlist) == 1: #checks if there is only 1 number
        return xlist[0]
    else:
        maxtemp = maximum(xlist[1:]) #recursively calls max on all but first num
        if maxtemp > xlist[0]: #compares and returns the greater number
            return maxtemp
        else:
            return xlist[0] 

def main():
    nums = eval(input("Enter a list of numbers: "))
    print("The max is: ", maximum(nums))

main()
