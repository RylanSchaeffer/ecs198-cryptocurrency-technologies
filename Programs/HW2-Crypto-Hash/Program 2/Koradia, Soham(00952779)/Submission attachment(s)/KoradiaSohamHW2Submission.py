'''
Name: Soham Koradia
Class: ECS 198F: Cryptocurrency in Python
HW Assignment: 2
'''

import hashlib
import math
import sys

def computeHash(inputFile):
    # Initialize a list for storing each transaction from the file
    try:
        transactionsList = open(inputFile, 'rt').read().split('\n')
    except FileNotFoundError:
        print("The file cannot be found. Please enter a valid name.")
        return

    # If there's a newline character at the end, account for it
    if len(transactionsList[len(transactionsList) - 1]) == 0:
        transactionsList = transactionsList[:len(transactionsList) - 1]

    nextLogOfTwo = math.log2(len(transactionsList))

    # If the number of transactions in the list is not a power of 2, then append the string 'null' into it until it is
    if not nextLogOfTwo.is_integer():
        # Find what the next log of two is
        nextLogOfTwo = math.ceil(math.log2(len(transactionsList)))
        targetNumOfList = int(math.pow(2, nextLogOfTwo))

        # And append 'null'
        for i in range(0, targetNumOfList - len(transactionsList), 1):
            transactionsList.append('null')
    else:
        nextLogOfTwo = int(nextLogOfTwo)
   
    # Encode each of the items in transactionsList to their corresponding representations in bytes
    for indexOfTrans in range(0, len(transactionsList), 1):
        transactionsList[indexOfTrans] = bytes(transactionsList[indexOfTrans], 'utf-8')
 
    hashes = []
    currLevelHash = list(transactionsList)
    nextLevelHash = []

    for j in range(0, len(currLevelHash), 1):
        hashOfEachElem = hashlib.sha256()
        hashOfEachElem.update(currLevelHash[j])

        nextLevelHash.append(hashOfEachElem)
    currLevelHash = nextLevelHash

    # Now start hashing and concatenating each pair of elements up till nextLogOfTwo
    for i in range(0, nextLogOfTwo, 1):
        nextLevelHash = []
        for j in range(0, len(currLevelHash) - 1, 2):
            hashOfFirstElem = currLevelHash[j].hexdigest()
            hashOfSecondElem = currLevelHash[j+1].hexdigest()

            bothElemsConcatenated = hashOfFirstElem + hashOfSecondElem
            hashOfBothElems = hashlib.sha256()
            hashOfBothElems.update(bytes(bothElemsConcatenated, 'utf-8'))

            nextLevelHash.append(hashOfBothElems)
        currLevelHash = nextLevelHash

    # Set hashes to be equal to currLevelHash
    hashes = currLevelHash

    # And return the hexdigest of the root hash
    return hashes[0].hexdigest()

def main():
    if len(sys.argv) == 2:
        transFileName = sys.argv[1]
        transFileHash = computeHash(transFileName)
        if not transFileHash == None:
            print(transFileName + ": " + transFileHash)
    else:
        print("Invalid number of command line arguments specified. Please enter the name of one transaction file.")

if __name__ == '__main__':
    main()
