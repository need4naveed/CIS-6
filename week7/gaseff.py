#program to calculate gas efficiency across a multi leg trip

print("Calculates fuel effieciency.")
odom1 = eval(input("Enter starting odometer value: "))
miles = []
gas_total = []

print("Enter a blank line when ready to calculate total.")
stop = input("Enter next odometer reading and gas used seperated by space: ")
while stop != "":
    odom2, gas = stop.split() #splits up 2 numbers seperated by space and assigns to variables
    odom2 = eval(odom2) #turn numbers from str to int
    gas = eval(gas)
    miles.append(odom2 - odom1) #add data from each leg onto lists
    gas_total.append(gas)
    odom1 = odom2
    stop = input("Enter next odometer reading and gas used seperated by space: ")

for i in range(len(miles)): 
    mpg = miles[i] / gas_total[i] #calculates total for each leg
    print("Leg",i,"your mpg was:",mpg) 
miles_total = sum(miles)
gas_sum = sum(gas_total)
print("Total MPG:",miles_total/gas_sum) #calculates and displays total mpg
