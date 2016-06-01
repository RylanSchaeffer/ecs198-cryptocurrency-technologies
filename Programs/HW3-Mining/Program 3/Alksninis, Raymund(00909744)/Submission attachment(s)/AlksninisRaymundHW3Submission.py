import hashlib
import math
import sys

def main():
    target = int(sys.argv[2])
    print("target is: ", target)
    infilename = sys.argv[1]
    
    infile = open(infilename)
    lines = infile.read().splitlines()

    if not (math.log2(len(lines))).is_integer():
        while len(lines) < (pow(2,math.ceil(math.log2(len(lines))))):
            lines.append("null")

    hashes = []
    for i in range(len(lines)):
        hashes.append(hashlib.sha256(lines[i].encode('utf-8')))

    targetFound = False
    nonce = 1
    while (not targetFound):
        if(nonce%1000 == 0):
            print("Testing nonce: ", nonce)
        hashcopy = hashes
        hashcopy[-1] = (hashlib.sha256(str(nonce).encode('utf-8')))
        
        while len(hashcopy) > 1:
            newlist = []
            for i in range(int(len(hashcopy)/2)):
                h = hashlib.sha256((hashcopy[2*i].hexdigest()).encode('utf-8'))
                h.update((hashcopy[(2*i)+1].hexdigest()).encode('utf-8'))
                newlist.append(h)
            hashcopy = newlist

        result = hashcopy[0].hexdigest()
        if (int(result[:target], 16) == 0):
            targetFound = True
        else:
            nonce += 1

    print(result)
    return nonce
