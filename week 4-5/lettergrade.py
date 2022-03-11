#program to translate a 0-5 grade to letter grade
def main():
    letterscale = "FFDCBA"
    quizgrade = int(input("Please enter the quiz grade on a scale from 0 to 100: "))
    rounded = round(quizgrade/20,-1)
    print(rounded)
    lettergrade = letterscale[rounded]
    print("Your quiz grade of {0} is equivilent to a letter grade of {1}.".format(quizgrade, lettergrade))
main()
