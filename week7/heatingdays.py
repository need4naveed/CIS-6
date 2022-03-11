#program to calculate hot and cool days given average daily temps in a file

def main():
    print("Hot/Cold day calculator")

    day = 1
    cooldays = 0
    hotdays = 0

    infile = open("temps.txt", "r")

    for line in infile:
        temp = eval(line)
        if temp != -100:
            if temp < 60:
                hotdays += 60 - temp
            elif temp > 80:
                cooldays += temp - 80
            day += 1
        else:
            break
    print("Cooling degree days:", cooldays)
    print("Heating degree days:", hotdays)

main()
            
        
