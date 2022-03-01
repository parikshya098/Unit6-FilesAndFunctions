def percentchange(todayprice, yesterdayprice):
    return ((todayprice - yesterdayprice) / (yesterdayprice)) * 100

stockfile = open("06.02 Stock.txt","r")
read = stockfile.read().split("\n")
print("{0:>10s}{1:>10s}".format("Price","Change"))
print("{0:>10s}{1:>10s}".format(read[0],""))

for i in range(1, len(read)):
    print("{0:>10s}{1:>10.2f}%".format(read[i],percentchange(float(read[i]),float(read[i-1]))))