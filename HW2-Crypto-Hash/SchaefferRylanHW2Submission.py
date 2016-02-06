__author__ = 'rylan'

# import cryptographic hashing library
import hashlib
import sys


def main(argv):

    # open transaction file
    file = open(argv[0], 'r')

    # split file into individual transactions
    transactions = file.read().rstrip('\n').split('\n')

    # close transaction file
    file.close()

    # hash each each transaction using SHA256
    hashes = map(hashlib.sha256, transactions)

    # iteratively calculate hash of children's hashes concatenated
    while len(hashes) != 1:
        print len(hashes)
        hashes = [hashlib.sha256(leftHash.hexdigest() + rightHash.hexdigest()) for leftHash, rightHash in zip(hashes[0::2], hashes[1::2])]

    # print and return hexidecimal digest
    root = hashes[0].hexdigest()
    print 'Root hash: ' + root
    return root

if __name__ == '__main__':
    main(sys.argv[1:])