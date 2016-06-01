import hashlib
import math
import sys

def main():
    infilename = sys.argv[1]
    
    infile = open(infilename)
    lines = infile.read().splitlines()

    if not (math.log2(len(lines))).is_integer():
        while len(lines) < pow(2,math.ceil(math.log2(len(lines)))):
            lines.append("null")
    hashes = []
    for i in range(len(lines)):
        hashes.append(hashlib.sha256(lines[i].encode('utf-8')))
        
    while len(hashes) > 1:
        newlist = []
        for i in range(int(len(hashes)/2)):
            h = hashlib.sha256((hashes[2*i].hexdigest()).encode('utf-8'))
            h.update((hashes[(2*i)+1].hexdigest()).encode('utf-8'))
            newlist.append(h)
        hashes = newlist

    return hashes[0].hexdigest()
