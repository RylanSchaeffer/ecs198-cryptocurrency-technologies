__author__ = 'rylan'

import hashlib
import math
import sys


def main(argv):

    # open transaction file
    file = open(argv[0], 'r')

    # read in target number of leading zeroes
    target = int(argv[1])

    # split file into individual transactions
    transactions = file.read().rstrip('\n').split('\n')

    # close transaction file
    file.close()

    # extend list of transactions until its length is a power of two minus one
    while not (math.log(len(transactions) + 2, 2)).is_integer():
        transactions.append("null")

    # append transaction for new block
    transactions.append('Rylan Schaeffer receives the newly mined coin')

    # initialize nonce to zero
    nonce = 0

    # append nonce to list of transactions
    transactions.append(str(nonce))

    # initialize binroot to binary string with no leading zeroes
    binroot = '1'

    # while puzzle has yet to be solved
    while len(binroot.split('1', 1)[0]) < target:

        # hash each each transaction using SHA256
        hashes = map(hashlib.sha256, transactions)

        # iteratively calculate hash of children's hashes concatenated
        while len(hashes) != 1:
            hashes = [hashlib.sha256(leftHash.hexdigest() + rightHash.hexdigest()) for
                      leftHash, rightHash in zip(hashes[0::2], hashes[1::2])]

        # return hexidecimal digest
        root = hashes[0].hexdigest()

        # convert from hexadecimal to binary
        binroot = bin(int(root, 16))[2:].zfill(len(root)*4)

        print binroot

        # increment nonce
        nonce += 1

        # replace previous nonce with new nonce
        transactions[-1] = str(nonce)

    return transactions


if __name__ == '__main__':
    main(sys.argv[1:])
