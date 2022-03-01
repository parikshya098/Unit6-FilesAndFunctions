fileA = open('06.05 CompareFileA.txt', 'r')
fileB = open('06.05 CompareFileB.txt', 'r')

lineNo = 1
differences = 0
linesFileA = fileA.readline()
linesFileB = fileB.readline()
  
while linesFileA != '' or linesFileB != '':
    linesFileA = linesFileA.rstrip()
    linesFileB = linesFileB.rstrip()
    if linesFileA != linesFileB:
        differences += 1
        print("Line: {} - File A: {}".format(lineNo,linesFileA))
        print()   
        print("Line: {} - File B: {}".format(lineNo,linesFileB))
        print()
    linesFileA = fileA.readline()
    linesFileB = fileB.readline()
    lineNo += 1
print("{} differences".format(differences))

fileA.close()
fileB.close()