__author__ = 'eric'

# import cryptographic hashing library
import hashlib
import math
import sys


def main(argv):   
    i = 0
    mine = 1
    
    j = 1
    check = "0"
    while j < int(argv[1]):
	    check = check + "0"
	    j = j + 1
 
    while (mine == 1):
	    # open transaction file
	    file = open(argv[0], 'r')

	    # split file into individual transactions
	    transactions = file.read().rstrip('\n').split('\n')

	    # close transaction file
	    file.close()

	    #Append Nonce
	    transactions.append(hashlib.sha256(str(i)).hexdigest())

	    # extend list of transactions until its length is a power of two
	    while not math.log(len(transactions), 2).is_integer():
		transactions.append("null")

	    # hash each each transaction using SHA256
	    hashes = map(hashlib.sha256, transactions)

	    # iteratively calculate hash of children's hashes concatenated
	    while len(hashes) != 1:
		hashes = [hashlib.sha256(leftHash.hexdigest() + rightHash.hexdigest()) for leftHash, rightHash in zip(hashes[0::2], hashes[1::2])]

	    # return hexidecimal digest
	    if hashes[0].hexdigest()[:int(argv[1])] == check:
		mine = 0
        	#print hashes[0].hexdigest()
		#print "WOAH"
		#print i
		return i
	    else:
		i = i + 1
	    if i > 9000000:
		print "Too many iterations: Quitting!"
		mine = 0
		return 1



if __name__ == '__main__':
    main(sys.argv[1:])
