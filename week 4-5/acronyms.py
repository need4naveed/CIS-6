def main():
    userwords = str(input("Enter the words separated by a space to be used for the acronym: "))
    words = userwords.split()
    for i in range(len(words)):
        newacronym = []
        word = words[i]
        for i in word:
            firstletter = word[0]
            newacronym.append(firstletter)
    print("The acronym is {0}".format(newacronym))

main()
