def main():
    print("Convers unicode nummbers to text")

    message = input("Please enter message to encode seperated by spaces: ")
    newm = ""
    for c in message.split():
        codenum = int(c)
        newm += chr(codenum)
    print("The decoded message is: ", newm)
main()

    
