import sys
import hashlib

def main():
    # Read transactions from file
    f = open(sys.argv[1])
    transactions = []
    for line in f:
        transactions.append(line[:-1]) # The [:-1] cuts off the newline
            
    # Make sure the number of transactions is a power of 2
    while ((len(transactions) & (len(transactions) - 1)) != 0) and len(transactions) != 0:
        transactions.append('null')
    
    # Hash through the Merkle tree
    temp1 = transactions
    while len(temp1) > 1:
        temp2 = []
        for index in range(len(temp1)):
            temp1[index] = hashlib.sha256(temp1[index]).hexdigest()
            if index % 2 != 0:
                temp2.append(temp1[index-1]+temp1[index])
        temp1 = temp2
    
    # Return root hash
    return hashlib.sha256(temp1[0]).hexdigest()
    
if __name__ == '__main__':
    main()
    