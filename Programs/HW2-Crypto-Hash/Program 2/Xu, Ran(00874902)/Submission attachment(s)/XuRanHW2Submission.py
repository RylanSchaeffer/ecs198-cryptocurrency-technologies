import hashlib
import sys
import math


def main():

    with open(str(sys.argv[1]),'rb') as inf:
        lines = inf.read().splitlines()
        length = len(lines)
        next_length = int(pow(2, math.ceil(math.log(length, 2))))

        while length < next_length:
            lines.append(b"null")
            length += 1

        lines[:] = [hashlib.sha256(transaction).hexdigest() for transaction in lines]

        while length != 1:
            length /= 2
            for index in range(0, length):
                lines[index] = hashlib.sha256(lines[index*2]+lines[index*2+1]).hexdigest()

        return lines[0]


if __name__ == "__main__":main()
