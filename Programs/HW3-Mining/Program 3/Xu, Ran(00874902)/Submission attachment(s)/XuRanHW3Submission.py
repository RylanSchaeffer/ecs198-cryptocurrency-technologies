import hashlib
import sys
import math


def main(argv):
    
    inf = open(argv[0],'r')
    nonce = '0' * int(argv[1])
    lines = inf.read().rstrip('\n').split('\n')
    inf.close()
    
    next_integer = 0
    my_result = 'null'
    
    
    
    while my_result.find(nonce) != 0:
        new_lines = lines[:]
        new_lines.append(str(next_integer))
        length = len(new_lines)
        new_lines[:] = [hashlib.sha256(transaction).hexdigest() for transaction in new_lines]
        
        while length != 1:
            length /= 2
            for index in range(0, length):
                new_lines[index] = hashlib.sha256(new_lines[index*2]+new_lines[index*2+1]).hexdigest()

        my_result = new_lines[0]
        next_integer += 1

    return next_integer - 1


if __name__ == "__main__":
    main(sys.argv[1:])
