
print("Calculates fuel effieciency.")
miles = []
gas_total = []
odom1 = 0

infile = open("trip.txt", "r")

for line in infile:
    odom2, gas = line.split() #splits up 2 numbers seperated by space and assigns to variables
    odom2 = eval(odom2) #turn numbers from str to int
    gas = eval(gas)
    miles.append(odom2 - odom1) #add data from each leg onto lists
    gas_total.append(gas)
    odom1 = odom2

for i in range(len(miles)): 
    mpg = miles[i] / gas_total[i] #calculates total for each leg
    print("Leg",i,"your mpg was:",mpg) 
miles_total = sum(miles)
gas_sum = sum(gas_total)
print("Total MPG:",miles_total/gas_sum) #calculates and displays total mpg
    
