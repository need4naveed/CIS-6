def main():
    print("Convers text to sequence of numbers")

    message = input("Please enter message to encode: ")

    print("Here are the Unicode codes: ")

    for c in message:
        print(ord(c), end=" ")

main()

         
