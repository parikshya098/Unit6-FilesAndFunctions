def FahrToCel(fahr):
    cel = (fahr - 32) * 5/9
    return cel

recordCounter = 0
inputfile = open("06.03 FTemps.txt","r")
outputfile = open("06.03 CTemps.txt","w")
for line in inputfile.readlines():
    temp = float(line.strip())
    celsius = FahrToCel(temp)
    outputfile.write(f"{celsius:.1f}\n")
    recordCounter += 1

print(recordCounter, "records written")