import hashlib
import math
import sys


def moreHash(hashList):
    newList = []
    for i,k in zip(hashList[0::2], hashList[1::2]):
        m = hashlib.sha256()
        m.update((i.hexdigest()).encode('UTF-8'))
        m.update((k.hexdigest()).encode('UTF-8'))
        newList.append(m)

    return newList

def initialHash(lines):
    firstHash = []
    for line in lines:
        m = hashlib.sha256(line)
        firstHash.append(m)
    return firstHash


def main():
    lines = open(sys.argv[1],"rb").read().splitlines()
    next_power_of_2 = pow(2,math.ceil(math.log2(len(lines))))
    nullstr = bytes("null", encoding="UTF-8")
    for num in range(len(lines), next_power_of_2 ):
        lines.append(nullstr)
        num += 1

    hashList = initialHash(lines)
    while (len(hashList) != 1):
        curList = moreHash(hashList)
        hashList = curList


    print(hashList[0].hexdigest())


if __name__ == '__main__':
  main()

