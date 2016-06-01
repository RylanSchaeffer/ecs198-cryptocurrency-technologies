import hashlib
import math
import sys

def main():
    hashlist = []
    diglist = []
    transactionlistobj = open(sys.argv[1])
    transactionlist = transactionlistobj.read()
    splittransactionlist = str.splitlines(transactionlist)


    nextpow2 = pow(2,math.ceil(math.log2(len(splittransactionlist))))
    for i in range(len(splittransactionlist),nextpow2):
        splittransactionlist.append("null") #splitting list and appending null


    for i in range(0,len(splittransactionlist)):
        hashlist.append(hashlib.sha256(splittransactionlist[i].encode('utf-8'))) #hashing initial list
        diglist.append(hashlist[i].hexdigest()) #generating initial digested hash


    for i in range(0,math.ceil(math.log2(nextpow2))): #for each power of 2
        for j in range(0,int(len(diglist)/2)): #for half the list
            sha256 = hashlib.sha256(diglist[j+j].encode('utf-8')+diglist[j+(j+1)].encode('utf-8'))
            diglist[j] = sha256.hexdigest()


    return diglist[0]

main()