import hashlib
import random
import re

print("Pex2 by Andrew Lee")
print("Sadly written in python and not Haskell")
print()
print("Starting Task 1...")
print()

fileOpen = open("samplefile.txt", "r+")
fileString = fileOpen.read()
fileOpen.close()

result = hashlib.md5(fileString.encode())
tinyresult = (result.hexdigest())[0:5]

print("Original file is: samplefile.txt")
print("Hash of the original file:", result.hexdigest())
print("Tiny hash of the original file:", tinyresult)
print("-----------------------------------")

counter = 0
numFound = 1

while(numFound <= 5):
    with open("words.txt", "r") as file:
        for line in file:
            counter += 1
            newline = line.rstrip()
            newString = fileString + (newline)

            newHash = hashlib.md5(newString.encode())
            newTinyHash = (newHash.hexdigest())[0:5]

            if(tinyresult == newTinyHash and numFound <= 5):
                print("Found collision after %d attempts: %d" %(counter,numFound))
                print("writing to file: collision" + str(numFound) + ".txt")
                print()

                newFile = open("collision" + str(numFound) + ".txt", "a")
                newFile.write(newString)
                newFile.close()

                numFound += 1

    lines = open("words.txt", "r").read().splitlines()
    randline = random.choice(lines)
    fileString += randline

print()
print("Starting Task 2...")
print()

fileTaskTwo = open("contract.txt", "r+")
stringTaskTwo = fileTaskTwo.read()
fileTaskTwo.close()

nfthash = hashlib.md5(stringTaskTwo.encode())
tinynft = (nfthash.hexdigest())[0:5]

print("Hash of the original file:", nfthash.hexdigest())
print("Tiny hash:", tinynft)

print("-----------------------------------")

nftnum = int(re.findall(r'\d+', stringTaskTwo)[0])
nftstring = stringTaskTwo.split('$')[0]
nftstring+='$'

price = 0
while (price < nftnum):
    newString = nftstring + str(price)

    newHash = hashlib.md5(newString.encode())
    newTinyHash = (newHash.hexdigest())[0:5]

    if(newTinyHash == tinynft):
        print("Found Hash collision with value $", price)
        print("new contract saved to file: newcontract.txt")

        newFile = open("newcontract.txt", "a")
        newFile.write(newString)
        newFile.close()

        break

    price += 1
