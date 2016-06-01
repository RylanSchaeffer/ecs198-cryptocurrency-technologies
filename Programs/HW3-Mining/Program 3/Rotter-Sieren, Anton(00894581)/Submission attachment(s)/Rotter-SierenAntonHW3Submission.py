import hashlib
import math
import sys
def main():
    transactionlistobj = open(sys.argv[1])
    transactionlist = transactionlistobj.read()
    splittransactionlist = str.splitlines(transactionlist)
    nonce = 0
    target = int(sys.argv[2])
    leadingzeroes = 0


    nextpow2 = pow(2,math.ceil(math.log2(len(splittransactionlist))))
    for i in range(len(splittransactionlist),nextpow2-1):
        splittransactionlist.append("null") #splitting list and appending null

    while (leadingzeroes < target):
        hashlist = []
        diglist = []
        noncestr = str(nonce)
        splittransactionlist.append(noncestr)
        for i in range(0,len(splittransactionlist)):
            hashlist.append(hashlib.sha256(splittransactionlist[i].encode('utf-8'))) #hashing initial list
            diglist.append(hashlist[i].hexdigest()) #generating initial digested hash


        for i in range(0,math.ceil(math.log2(nextpow2))): #for each power of 2
            for j in range(0,int(len(diglist)/2)): #for half the list
                sha256 = hashlib.sha256(diglist[j+j].encode('utf-8')+diglist[j+(j+1)].encode('utf-8'))
                diglist[j] = sha256.hexdigest()
        for i in range(0,len(diglist[0])):
            if diglist[0][i] == '0':
                leadingzeroes = leadingzeroes + 1
            else:
                break
        if leadingzeroes >= target:
            return nonce
        else:
            nonce = nonce + 1
            leadingzeroes = 0
            splittransactionlist.pop()



    return nonce

main()