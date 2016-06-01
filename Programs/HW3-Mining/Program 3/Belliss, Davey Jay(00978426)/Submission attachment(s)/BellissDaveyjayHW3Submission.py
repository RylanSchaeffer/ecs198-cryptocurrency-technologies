__author__ = 'rylan'
__editedBy__ = 'Davey Jay'
# import cryptographic hashing library
import hashlib
import math
import sys


def main(argv):
    # open transaction file
    file = open(argv[0], 'r')

    # split file into individual transactions
    transactions = file.read().rstrip('\n').split('\n')

    # close transaction file
    file.close()
    hashes = map(hashlib.sha256, transactions)
    counter = 0
    x = 0

    while not math.log(len(transactions) + 1, 2).is_integer():
        transactions.append("null")
    transactions.append(str(x))
    while 1==1:
      counter = 0
      transactions[len(transactions)-1] = str(x)
   
      # hash each each transaction using SHA256
      hashes = map(hashlib.sha256, transactions)

      # iteratively calculate hash of children's hashes concatenated
      while len(hashes) != 1:
          hashes = [hashlib.sha256(leftHash.hexdigest() + rightHash.hexdigest()) for leftHash, rightHash in zip(hashes[0::2], hashes[1::2])]
      num = 0
      counter = 0
      while hashes[0].hexdigest()[num] == "0":
        counter+=1
        num+=1
        if str(counter) == argv[1]: # Enough zeroes
          return x
      x+=1
      # return hexidecimal digest

if __name__ == '__main__':
    main(sys.argv[1:])
