'''
Name: Soham Koradia
Class: ECS 198F: Cryptocurrency in Python
HW Assignment: 3
'''

import hashlib
import math
import sys

def rightNumOfLeadingZeroesPresent(numToCheckFor, hashToProcess):
    stringRep = str(hashToProcess)
    count = 0

    for i in range(0, len(stringRep), 1):
        if not stringRep[i] == '0':
            break
        else:
            count += 1

    if not numToCheckFor == count:
        return False

    return True

def computeHash(inputFile, numOfLeadingZeroes):
    # Initialize a list for storing each transaction from the file
    try:
        transactionsList = open(inputFile, 'rt').read().split('\n')
    except FileNotFoundError:
        print("The file cannot be found. Please enter a valid name.")
        return

    # If there's a newline character at the end, account for it
    if len(transactionsList[len(transactionsList) - 1]) == 0:
        transactionsList = transactionsList[:len(transactionsList) - 1]

    nextLogOfTwo = math.log2(len(transactionsList) + 1)

    # If the number of transactions in the list is not a power of 2, then append the string 'null' into it until it is
    if not nextLogOfTwo.is_integer():
        # Find what the next log of two is
        nextLogOfTwo = math.ceil(math.log2(len(transactionsList)))
        targetNumOfList = int(math.pow(2, nextLogOfTwo)) - 1 # Only add 'null' until the length of the transactions list is 2^n - 1

        # And append 'null'
        for i in range(0, targetNumOfList - len(transactionsList), 1):
            transactionsList.append('null')
    else:
        nextLogOfTwo = int(nextLogOfTwo)

    # Now add an integer towards the end of the list, and check to see if the final hash generated has the user specified number of leading zeroes
    # if not, then increment the integer and try the hashing algorithm with that as the last entry to the list instead
    nonce = -1
    finalHash = ''
    origTransactionsList = list(transactionsList)

    while not rightNumOfLeadingZeroesPresent(numOfLeadingZeroes, finalHash):
        # Increment the nonce at the start of the loop
        nonce += 1
        # And append it to the end of the transactions list
        transactionsList = origTransactionsList + [str(nonce)]
 
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
        finalHash = hashes[0].hexdigest()

    return finalHash, nonce

def main():
    if len(sys.argv) == 3:
        transFileName = sys.argv[1]
        numOfLeadingZeroes = eval(sys.argv[2])

        if numOfLeadingZeroes == 0:
            print("Enter a greater number of leading zeroes for the hash to have.")
            exit()

        hashAndNonce = computeHash(transFileName, numOfLeadingZeroes)
        transFileHash = hashAndNonce[0]
        nonceVal = str(hashAndNonce[1])
        if not transFileHash == None:
            print(transFileName + ": " + transFileHash)
            print("The value of the nonce was found to be " + nonceVal)
    else:
        print("Invalid number of command line arguments specified. Please enter the name of one transaction file.")

if __name__ == '__main__':
    main()
