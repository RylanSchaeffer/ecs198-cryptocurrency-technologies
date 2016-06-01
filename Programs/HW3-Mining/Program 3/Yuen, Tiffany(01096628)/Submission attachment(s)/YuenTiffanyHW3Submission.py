# import cryptographic hashing library
import hashlib
import math
import sys


def main():

    # open transaction file
    file = open(sys.argv[1], 'r')

    # split file into individual transactions
    transactions = file.read().rstrip('\n').split('\n')

    # close transaction file
    file.close()
        
    # extend list of transactions until its length is a power of two
    while not math.log(len(transactions), 2).is_integer():
        transactions.append("null")
        
    number = sys.argv[2]
    num_zero = 9999999999999
    while num_zero != number:
        # hash each each transaction using SHA256
        hashes = map(hashlib.sha256, transactions)

        # iteratively calculate hash of children's hashes concatenated
        while len(hashes) != 1:
            hashes = [hashlib.sha256(leftHash.hexdigest() +
                                     rightHash.hexdigest()) for leftHash,
                      rightHash in zip(hashes[0::2], hashes[1::2])]

        merkle_root = hashes[0].hexdigest()

        nonce = 99

        num_zero = len(merkle_root) - len(merkle_root.lstrip('0'))
        nonce += 1
        del transactions[-1]
        nonce = str(nonce)
        transactions.append(nonce)

    return nonce


if __name__ == '__main__':
    main()
