#testing strings

def main():
    name1 = input("enter first name:")
    print("Hello", name1)
    name2 = input("enter last name:")
    namefull = name1 + name2
    print(namefull * 3)
    print(namefull[:4] + "sucks" + namefull[4:])
                

main()
