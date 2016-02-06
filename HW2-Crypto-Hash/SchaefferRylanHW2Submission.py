__author__ = 'rylan'

# import cryptographic hashing library
import hashlib

transactions = [str(item) for item in range(0, 16)]

def main(transactionFile):

    # open transaction file
    file = open(transactionFile, 'r')

    transactions = file.read().split('\n')

    # hash each each transaction using SHA256
    hashTree = map(hashlib.sha256, transactions)

    # iteratively calculate hash of children's hashes
    while len(hashTree) != 1:
        for leftHash, rightHash in zip(hashTree[0::2], hashTree[1::2]):
            print leftHash, rightHash
            hashTree = [hashlib.sha256(leftHash.hexdigest() + rightHash.hexdigest())]

    print hashTree

    return hashTree

if __name__ == '__main__':
    main()