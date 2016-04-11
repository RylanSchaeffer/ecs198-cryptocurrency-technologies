__author__ = 'rylan'

import random
import rsa

file = open('transactions5.txt', 'w')

# generate random number between 4 and 10, inclusive
n = random.randint(3, 6)

adjustment = random.randint(0, 2**(n-1))

print n
print str(adjustment) + '\n'

# generate 2^n random transactions
for ith in range(0, 2**n - adjustment):

    print ith

    # generate public keys for the transactions
    (publicKeySender, privateKeySender) = rsa.newkeys(1048)
    (publicKeyReceiver, privateKeyReceiver) = rsa.newkeys(1048)

    # generate transfer amount
    transferAmt = random.randint(0, 10000)

    # generate message
    msg = str(publicKeySender) + ' transfers $' + str(transferAmt) + ' to ' + str(publicKeyReceiver)

    # write message and signature to transaction file
    file.write(msg + '\n')

file.close()
