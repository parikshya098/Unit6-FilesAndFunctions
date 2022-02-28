from math import pi
def diameter(r):
    return (2 * r)
def circumference(r):
    return (2 * pi * r)
def area(r):
    return (pi * r * r)

print("{:>15s}{:>15s}{:>15s}{:>15s}".format("Radius" , "Diameter" , "Circumference", "Area"))

testfile = open("06.01 Radius.txt")
x = testfile.readline()
while x != "":
    radius = float(x)
    x = testfile.readline()
    print("{:15.5f}{:15.5f}{:15.5f}{:15.5f}".format(radius, diameter(radius),circumference(radius), area(radius)))

testfile.close()