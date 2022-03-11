def main():
    userwords = str(input("Enter the words separated by a space to be used for the acronym: "))
    print("Your acronym is:", "".join(acronym(userwords)))

def acronym(w):
    words = w.split()
    newacronym = []
    for i in range(len(words)):
        word = words[i]
        firstletter = word[0]
        newacronym.append(firstletter)
    return newacronym

main()
