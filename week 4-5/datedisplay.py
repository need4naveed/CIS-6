def main():
    print("Displays month and day of entered date")
    datenum = input("Please enter the date in mm/dd/yyyy format: ")
    datemonth, dateday, dateyear = datenum.split("/")

    months = ["Jan","Feb","Mar","Apr","May","Jun",
              "Jul","Aug","Sep","Oct","Nov","Dec"]
    monthnum = months[int(datemonth) - 1]
    
    print("The date is:", monthnum, dateday + ", " + dateyear)
main()
