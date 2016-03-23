__author__ = 'rylan'

import random
import rsa

file = open('transactions.txt', 'w')

# generate random number between 4 and 10, inclusive
n = random.randint(4, 6)

# generate 2^n random transactions
for ith in range(0, 2**n):

    print ith

    # generate public keys for the transactions
    (publicKeySender, privateKeySender) = rsa.newkeys(1048)
    (publicKeyReceiver, privateKeyReceiver) = rsa.newkeys(1048)

    # generate transfer amount
    transferAmt = random.randint(0, 10000)

    # generate message
    msg = str(publicKeySender) + ' transfers $' + str(transferAmt) + ' to ' + str(publicKeyReceiver)

    # TODO: Figure out what to do when signature generates newline characters
    # write message and signature to transaction file
    file.write(msg + ' Signed: ' + rsa.sign(msg, privateKeySender, 'SHA-256') + '\n')

file.close()
