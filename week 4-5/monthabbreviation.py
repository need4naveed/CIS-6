#print abbreviation of a month given its number
import random
size = []
for i in range(5):
    n = random.randint(1,10)
    size.append(n)
print(size)
def main():
    months = "JanFebMarAprMayJunJulAugSepOctNovDec"
    monthnum = int(input("Enter a number between 1-12: "))
    pos = (monthnum - 1) * 3
    monthAb = months[pos:pos+3]
    print(monthAb)
    
main()
