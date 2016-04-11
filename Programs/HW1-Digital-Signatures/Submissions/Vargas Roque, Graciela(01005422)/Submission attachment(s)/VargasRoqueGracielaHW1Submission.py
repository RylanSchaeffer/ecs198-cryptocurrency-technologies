# ECS 198F Homework #1

import rsa
import os
import sys
#import VargasRoqueGracielaHW1Submission

def main():
    (pcKey, pKey) = rsa.newkeys(1024)
    messg = 'I, Graciela Vargas Roque, signed this message!'
    messg = messg.encode('utf-8')
    sig = rsa.sign(messg, pKey, 'SHA-256')

    return messg, sig, pcKey

if __name__ == '__main__': #if this is the main program run
    main() #run the main function
    
