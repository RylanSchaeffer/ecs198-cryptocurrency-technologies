# ECS 198F
# Program 1
# Kevin Tran

import sys
import rsa

def main():
    message = 'I, Kevin Tran, signed this sentence!'
    if sys.version_info[0] == 3:
        message = message.encode('utf-8')
        
    (publicKey, privateKey) = rsa.newkeys(1024)
    signature = rsa.sign(message, privateKey, 'SHA-1')
    return(message, signature, publicKey)

if __name__ == '__main__':
    main()
