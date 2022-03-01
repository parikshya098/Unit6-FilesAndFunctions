readfile = "06.04 EmptyLinesInput.txt"
writefile = "06.04 EmptyLinesOutput.txt"

output = open(writefile,"w")
read_count = 0
write_count = 0

f = open(readfile,"r")
for line in f:
    read_count += 1
    if line.strip():
        write_count += 1
        output.write(line)
output.close()

print(read_count,'records read')
print(write_count,'records written')