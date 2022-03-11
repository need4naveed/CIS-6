

def main():

    infile = open("names.txt", "r")

    for line in infile:
        print(line,end="")

    infile.close()

main()
