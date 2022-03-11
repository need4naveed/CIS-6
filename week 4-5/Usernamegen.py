def main():

    print("Program creates usernames from a file of names\n")

    infile = open("names.txt", "r")
    outfile = open("unames.txt", "w")

    for line in infile:
        first, last = line.split()
        
        uname = first[0] + last[:7]
        uname = uname.lower()

        print(line + ": " + uname)
        print(uname, file=outfile)

    infile.close()
    outfile.close()

    print("\nUsernames have been written to unames.txt")

main()
                                
