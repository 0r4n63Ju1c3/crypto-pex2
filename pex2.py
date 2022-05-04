import hashlib
import random
import re

print("Pex2 by Andrew Lee")
print("Sadly written in python and not Haskell")
print()
print("Starting Task 1...")
print()

#opening and reading file
fileOpen = open("samplefile.txt", "r+")
fileString = fileOpen.read()
fileOpen.close()

#hash file and find first 5 characters
result = hashlib.md5(fileString.encode())
tinyresult = (result.hexdigest())[0:5]

print("Original file is: samplefile.txt")
print("Hash of the original file:", result.hexdigest())
print("Tiny hash of the original file:", tinyresult)
print("-----------------------------------")

#helper variables, counter keeps track of words and numFound is number found
counter = 0
numFound = 1

#loop until you find 5 collisions
while(numFound <= 5):
    with open("words.txt", "r") as file:
        #loop through dictionary and append to end of string
        for line in file:
            counter += 1
            newline = line.rstrip()
            newString = fileString + (newline)

            #new hash values
            newHash = hashlib.md5(newString.encode())
            newTinyHash = (newHash.hexdigest())[0:5]

            #if collision is found, print and write to file, add oen to f
            if(tinyresult == newTinyHash and numFound <= 5):
                print("Found collision after %d attempts: %d" %(counter,numFound))
                print("writing to file: collision" + str(numFound) + ".txt")
                print()

                newFile = open("collision" + str(numFound) + ".txt", "w")
                newFile.write(newString)
                newFile.close()

                numFound += 1

    #when end of file is reached, append random line from dictionary
    lines = open("words.txt", "r").read().splitlines()
    randline = random.choice(lines)
    fileString += randline

print()
print("Starting Task 2...")
print()

#open nft contract file
fileTaskTwo = open("contract.txt", "r+")
stringTaskTwo = fileTaskTwo.read()
fileTaskTwo.close()

#find hash values
nfthash = hashlib.md5(stringTaskTwo.encode())
tinynft = (nfthash.hexdigest())[0:5]

print("Hash of the original file:", nfthash.hexdigest())
print("Tiny hash:", tinynft)

print("-----------------------------------")

#regex to parse file at $ and find price
nftnum = int(re.findall(r'\d+', stringTaskTwo)[0])
nftstring = stringTaskTwo.split('$')[0]
nftstring+='$'

#loop while new price is less than value parsed in contract
price = 0
while (price < nftnum):
    newString = nftstring + str(price)

    #new hash values
    newHash = hashlib.md5(newString.encode())
    newTinyHash = (newHash.hexdigest())[0:5]

    #if hash collission print to file
    if(newTinyHash == tinynft):
        print("Found Hash collision with value $", price)
        print("new contract saved to file: newcontract.txt")

        newFile = open("newcontract.txt", "w")
        newFile.write(newString)
        newFile.close()

        break

    price += 1
