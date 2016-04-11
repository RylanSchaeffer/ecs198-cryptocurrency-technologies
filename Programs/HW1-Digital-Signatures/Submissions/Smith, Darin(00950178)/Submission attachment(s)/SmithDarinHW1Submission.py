#!/usr/bin/env python

# import modules used here -- sys is a very standard one
import sys

import rsa as rsa


def main():
    (pubk, privk) = rsa.newkeys(1024, poolsize=2)
    mesg = 'I, Darin Smith, signed this sentence'
    mesg = mesg.encode('utf-16')
    sig = rsa.sign(mesg, privk, 'SHA-256')
    #print(signature)
    #print(pubkey)
    #print(rsa.verify(msg, signature, pubkey))
    # Above(commented out) is the verifier function found in documentation. Returned true.

    return mesg, sig, pubk


# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()
