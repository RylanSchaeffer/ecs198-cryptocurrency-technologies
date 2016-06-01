import math
import sys
import hashlib


def main():

    lines = open(sys.argv[1], 'r').read().splitlines()
    next_power_of_2 = pow(2, math.ceil(math.log(len(lines), 2)))
    number_of_appends = int(next_power_of_2 - len(lines))

    #appends useless strings to allow length of 2^^x
    for x in range(number_of_appends):
        lines.append('null')

    #initial hash for all the values
    for x in range(len(lines)):
        a = hashlib.sha256()
        a.update(lines[x])
        lines[x] = a.hexdigest()
    length = len(lines)

    while length != 1: # reached the root
        x = 0
        for hash1, hash2 in zip(lines[0::2], lines[1::2]): #lines[0::2] creates subset collection of elements that (index % 2 == 0)
            a = hashlib.sha256()
            a.update(hash1)
            a.update(hash2)
            lines[x] = a.hexdigest() #updates the lines array for re-use
            x += 1
        length /= 2

    return lines[0]

main()
