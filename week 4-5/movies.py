

def main():
    
    fname = "movies.txt"

    outfile = open(fname, "a")
    
    for i in range(3):
        movie = input("Enter a movie name: ")
        #print(movie, file = outfile)
        outfile.write(movie + "\n")

    outfile.close()

main()
