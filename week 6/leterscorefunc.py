#This program converts an exam grade from a number to the letter grade"

def letter(score):
    if score >=90:
        return 'A'
    elif score >=80:
        return 'B'
    elif score >=70:
        return "C"
    elif score >=60:
        return "D"
    elif score <60:
        return "F"

def main():
    print("This program converts an exam grade from a number to the letter grade")
    n = eval(input("Enter the exam score on a 0-100 scale: "))
    print("Your letter grade is:", letter(n))

main()
