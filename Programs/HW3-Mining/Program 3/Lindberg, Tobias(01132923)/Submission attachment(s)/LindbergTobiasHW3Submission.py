import sys
import hashlib

def main():
    # Read transactions from file
    f = open(sys.argv[1])
    transactions = []
    for line in f:
        transactions.append(line[:-1]) # The [:-1] cuts off the newline
    
    # Define variables needed for iteration
    n = int(sys.argv[2])
    target = ('0' * ((n/len('0'))+1))[:n]
    roothash = ""
    nonce = 0
    
    # Make sure the number of transactions is a power of 2
    while ((len(transactions) & (len(transactions) - 1)) != 0) and len(transactions) != 0:
        transactions.append('null')
    
    # Hash left half of Merkle tree
    temp3 = transactions[:len(transactions)/2]
    while len(temp3) > 1:
        temp4 = []
        for index in range(len(temp3)):
            temp3[index] = hashlib.sha256(temp3[index]).hexdigest()
            if index % 2 != 0:
                temp4.append(temp3[index-1]+temp3[index])
        temp3 = temp4
    lefthash = hashlib.sha256(temp3[0]).hexdigest() 
    
    # Iterate as long as the roothash does not start with n zeros 
    while not roothash.startswith(target):
        
        # Try a new integer each iterations following the pattern 0,1,-1,2,-2,...
        transactions[-1] = str(nonce)
        if nonce <= 0:
            nonce = -nonce + 1
        else:
            nonce = -nonce
    
        # Hash through the Merkle tree
        temp1 = transactions[len(transactions)/2:]
        while len(temp1) > 1:
            temp2 = []
            for index in range(len(temp1)):
                temp1[index] = hashlib.sha256(temp1[index]).hexdigest()
                if index % 2 != 0:
                    temp2.append(temp1[index-1]+temp1[index])
            temp1 = temp2
        righthash = hashlib.sha256(temp1[0]).hexdigest()
        
        roothash = hashlib.sha256(lefthash+righthash).hexdigest()
    
    # Return root hash
    print
    print 'Nonce: {}'.format(nonce)
    print 'Roothash: {}'.format(roothash)
    print
    return nonce
    
if __name__ == '__main__':
    main()
    