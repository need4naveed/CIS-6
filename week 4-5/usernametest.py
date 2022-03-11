#Program to generate username using
#first two letters of first and last names
#last four digits of student id

def main():
    first = input("Enter first name (lowercase): ")
    last = input("Enter last name (lowercase): ")
    sid = input("Enter student id: ")
    user = first[:2] + last[:2] + sid[-4:]
    print("Username:", user)

main()
