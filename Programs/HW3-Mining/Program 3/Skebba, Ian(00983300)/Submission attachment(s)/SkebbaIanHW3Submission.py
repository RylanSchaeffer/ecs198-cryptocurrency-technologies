# import cryptographic hashing library
import hashlib
import math
import sys


def main(argv):
    flag = 0
    x = 0
    target = int(argv[1])
    while flag == 0:
        # open transaction file
        file = open(argv[0], 'r')

        # split file into individual transactions
        transactions = file.read().rstrip('\n').split('\n')

        # close transaction file
        file.close()

        # extend list of transactions until its length is a power of two
        while not (math.log(len(transactions), 2).is_integer() - 1):
            transactions.append("null")

        transactions.append(str(x))

        # hash each each transaction using SHA256
        hashes = map(hashlib.sha256, transactions)

        # iteratively calculate hash of children's hashes concatenated
        while len(hashes) != 1:
            hashes = [hashlib.sha256(leftHash.hexdigest() + rightHash.hexdigest()) for leftHash, rightHash in zip(hashes[0::2], hashes[1::2])]

        # return hexidecimal digest
        correct = hashes[0].hexdigest()
        counter = 0
        for b in range(0, target):
            if (correct[b] == '0'):
                counter = counter + 1
        if counter != target:
            x = x + 1
            continue
        else:
            return x


if __name__ == '__main__':
    main(sys.argv[1:])
