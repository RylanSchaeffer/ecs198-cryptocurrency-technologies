__author__ = 'ali'

# import cryptographic hashing library
import hashlib
import math
import sys


def main(argv):

    # open transaction file
    file = open(argv[0], 'r')

    target = argv[1]

    nonce = 0


    # split file into individual transactions
    transactions = file.read().rstrip('\n').split('\n')

    # close transaction file
    file.close()

    # extend list of transactions until its length is a power of two
    while not math.log(len(transactions), 2).is_integer():
        transactions.append("null")

    



    # hash each each transaction using SHA256
    hashes = map(hashlib.sha256, transactions)

    

    # iteratively calculate hash of children's hashes concatenated
    while len(hashes[0].hexdigest()[:target]) != target:

        transactions.append(hashlib.sha256(nonce))

        while len(hashes) != 1:
        
            hashes = [hashlib.sha256(leftHash.hexdigest() + rightHash.hexdigest()) for leftHash, rightHash in zip(hashes[0::2], hashes[1::2])]
            nonce = nonce + 1


    # return hexidecimal digest
    return hashes[0].hexdigest()
    return nonce


if __name__ == '__main__':
    main(sys.argv[1:])