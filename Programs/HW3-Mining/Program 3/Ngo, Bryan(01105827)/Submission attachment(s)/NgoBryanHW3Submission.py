__author__ = 'rylan'
#Original author: Rylan, modified by Bryan for P3
# import cryptographic hashing library

import hashlib
import math
import sys


def main(argv):

    # open transaction file
    file = open(argv[0], 'r')
    lead = argv[1]

    # split file into individual transactions
    transactions = file.read().rstrip('\n').split('\n')

    # close transaction file
    file.close()

    # extend list of transactions until its length is a power of two
    while not math.log(len(transactions), 2).is_integer():
        transactions.append('null')

    # hash each each transaction using SHA256
    hashes = map(hashlib.sha256, transactions)

    # split the tree into left and right halves.
    hashesL = []
    hashesR = []
    length = len(hashes)/2
    for x in range(length):
        hashesL.append(hashes[x])

    hashes.reverse()

    for x in range(length):
        hashesR.append(hashes[x])

    hashesR.reverse()


    # iteratively calculate hash of children's hashes concatenated LEFT SIDE
    while len(hashesL) != 1:
        hashesL = [hashlib.sha256(leftHash.hexdigest() + rightHash.hexdigest()) for leftHash, rightHash in zip(hashesL[0::2], hashesL[1::2])]

    # iteratively calculate hash of children's hashes concatenated RIGHT SIDE
    while len(hashesR) != 1:
        hashesR = [hashlib.sha256(leftHash.hexdigest() + rightHash.hexdigest()) for leftHash, rightHash in zip(hashesR[0::2], hashesR[1::2])]

    # return hexidecimal digest

    #print(hashes[0].hexdigest())
    return hashes[0].hexdigest()


if __name__ == '__main__':
    main(sys.argv[1:])
