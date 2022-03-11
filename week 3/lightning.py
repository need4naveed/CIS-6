#Program to determine the distance to a lightning strike in miles

def main():
    print("This program will determine the distance to a lightning strike in miles.")
    print()
    light = eval(input("Enter the time in seconds between seeing the lightning and hearing the thunder: "))
    dist = light * 1100 / 5280
    print("The lightning strike was", dist, "miles away")

main()
