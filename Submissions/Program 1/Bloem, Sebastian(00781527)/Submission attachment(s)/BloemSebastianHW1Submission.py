# ECS198 Cryptocurrency Technologies
# Programming Assignment #1
# Sebastian Bloem 998223779
#
# Teacher: Rylan Schaeffer (ryschaeffer@ucdavis.edu)
# Teacher: Vincent Yang (vinyang@ucdavis.edu)
#
# By Thursday 4/7 at 4:10 pm, please submit a Python script with one function,
# called main. The main() function should takes no input and should return
# three pieces of information:
# (1) the message 'I, <your name>, signed this sentence!'
# (2) your digital signature of the message using Python's rsa package
# (3) your public key
# My main() function ends with the line:
# return msg, signature, publicKey
#
# This program was tested on CSIF server pc1 as per following output:
#  >>> import rsa
#  >>> import BloemSebastianHW1Submission
#  >>> (msg, signature, pubkey) = BloemSebastianHW1Submission.main()
#  returned variables are: msg, signature, public_key
#  >>> rsa.verify(msg, signature, pubkey)
#  True
#######################################################################
# Misc Info:
#######################################################################
# The following code can be copy and pasted into the Python console to
# test the output of this program:
#
# import rsa
# import BloemSebastianHW1Submission
# (msg, signature, pubkey) = BloemSebastianHW1Submission.main()
# rsa.verify(msg, signature, pubkey)
#
#######################################################################
# imports
#######################################################################
import rsa


def main():
    # The code is run in a try...except block so only clean signature results.
    # This helped in troubleshooting the .encode dealeo for windows environment.
    try:
        (pub_key, priv_key) = rsa.newkeys(2048)
        #  Added .encode for windows environment. Still works on CSIF servers.
        msg = "I, Sebastian Bloem, signed this sentence".encode('utf-8')
        signature = rsa.sign(msg, priv_key, 'SHA-256')
        print('returned variables are: msg, signature, public_key')
        return msg, signature, pub_key
    except:
        print('There was an error signing message')
        exit()

if __name__ == '__main__':
    main()
