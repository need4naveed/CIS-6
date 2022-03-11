

def main():
    months = ["Jan","Feb","Mar","Apr","May","Jun",
              "Jul","Aug","Sep","Oct","Nov","Dec"]
    monthnum = int(input("Enter a number between 1-12: "))
    monthAb = months[monthnum - 1]
    print("The abbreviation is " monthAb)

main()
