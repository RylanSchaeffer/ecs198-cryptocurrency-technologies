__author__ = 'Chengeng'

import math
import hashlib
import sys

def main():
    hash = []
    filename = 'transactions1.txt'
    with open(filename, 'rb') as f:
        file = f.read()
    for lines in file:
        hash.append(lines)
    m = []
    for lines in sorted(hash):
        m.append(lines)
    #print(m)
    m = pow(2, math.ceil(math.log2(len(m))))
    m = hashlib.sha256()
    hashes = []
    hashes.append(m)
    print(filename, ': ', hashes[0].hexdigest().encode('utf-8'))
    return hashes[0].hexdigest()

main()
