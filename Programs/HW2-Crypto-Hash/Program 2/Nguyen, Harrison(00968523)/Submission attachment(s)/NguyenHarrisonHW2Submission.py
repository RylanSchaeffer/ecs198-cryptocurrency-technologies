import sys
import math
import hashlib

def main():

    content = open(sys.argv[1], 'rb').read().splitlines()

    next_power_of_2 = pow(2,math.ceil(math.log2(len(content))))

    nullstr = bytes('null', encoding='utf-8')

    while len(content) != next_power_of_2:
        content.append(nullstr)

    hashes = []

    hashes = [hashlib.sha256(line) for line in content]

    while len(hashes) != 1:
        new_hashes = []
        for index in range(0, len(hashes), 2):
            hash1, hash2 = hashes[index], hashes[index + 1]
            hash1, hash2 = hashlib.sha256(hash1), hashlib.sha256(hash2)
            combined_hash = (hash1.hexdigest()).encode('utf-8') + (hash2.hexdigest()).encode('utf-8')
            new_hashes.append(combined_hash)

    return new_hashes

main()

