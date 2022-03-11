def main():
    print("Convers unicode nummbers to text")

    message = input("Please enter message to encode seperated by spaces: ")
    chars = []
    for c in message.split():
        codenum = int(c)
        chars.append(chr(codenum))
    print(chars)

    newm = "".join(chars)
    
    print("The decoded message is: ", newm)
main()

    
