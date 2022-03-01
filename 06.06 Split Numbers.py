def isEven(n):
    return n % 2 == 0  
def isOdd(n):
    return n % 2 != 0  
def isPrime(n):
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    if i == n:
        return True

f1 = open("06.06 Numbers.txt", 'r')
f2 = open("06.06 Evennumbers.txt", 'w')
f3 = open("06.06 Oddnumbers.txt", 'w')
f4 = open("06.06 Primenumbers.txt", 'w')
evenCount = 0
oddCount = 0
primeCount = 0
totalnumbers = 0

for number in f1.readlines():
    number = int(number)
    if isEven(number):
        f2.write(str(number) + "\n")
        evenCount += 1
    elif isOdd(number):
        f3.write(str(number) + "\n")
        oddCount += 1
    if isPrime(number):
        f4.write(str(number) + "\n")
        primeCount += 1
    totalnumbers += 1

f1.close()
f2.close()
f3.close()
f4.close()

print(f"{evenCount} even numbers")
print(f"{oddCount} odd numbers")
print(f"{primeCount} prime numbers")
print(f"{totalnumbers} numbers read")