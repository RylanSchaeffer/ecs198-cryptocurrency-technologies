import sys
import hashlib
import math

def main():
    fileHashes = []
    # Read in file from command prompt and store each line as a str in list
    with open(sys.argv[1], 'rb') as f:
        fileContents = f.read()
        for lines in fileContents:
            fileHashes.append(lines)
            
    f.close()
    listLen = len(fileHashes)

    # Adjust block of hashes until it reaches the smaller 2**n > listLen
    power = int (math.ceil(math.log (listLen, 2) ))
    if power %2 != 0:
        power += 1
    listLen1 = 2 ** power
    listLenDiff = listLen1 - listLen

    # Append to the end of the block
    for i in range(0,listLenDiff):
        fileHashes.extend(fileHashes[-1:])
        
    hashes = []
    # Group the items in twos to concatinate them and create new hash
    for k in [fileHashes[x:x+2] for x in range(0, len(fileHashes), 2)]:
        # Hast the strings
        k[0] = hashlib.sha256((k[0]).encode('UTF-8'))
        k[1] = hashlib.sha256((k[1]).encode('UTF-8'))
        w = (k[0]).hexdigest()
        y = (k[1]).hexdigest()
        z = w + y
        hasher = hashlib.sha256(z.encode('UTF-8'))
        hashes.append(hasher)

    while len(hashes) != 1:
        length = len(hashes)
        for j in [hashes[i:i+2] for i in range(0, len(hashes), 2)]:
            a = (j[0]).hexdigest()
            b = (j[1]).hexdigest()
            c = a + b
            hasher = hashlib.sha256(c.encode('UTF-8'))
            hashes.append(hasher)
        # Delete previous hashe objects so the next hashing is only for the new
        # hash objects
        del hashes[0:length]

    # Return last hash       
    return hashes[0].hexdigest()
