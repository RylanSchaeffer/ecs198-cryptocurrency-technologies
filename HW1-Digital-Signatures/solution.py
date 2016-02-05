__author__ = 'rylan'

# import RSA module
import rsa

# generate public and private keys
(pubkey, privkey) = rsa.newkeys(1048)

# create message to digitally sign
msg = 'I, Rylan Schaeffer, signed this sentence!'

# hash the message using SHA-256, then sign the hash using private key
signature = rsa.sign(msg, privkey, 'SHA-256')

# create and open submission file
file = open('hw1-submission.txt', 'w')

# write signed message to submission file
file.write('Signed Message: ' + signature + '\n')

# write public key to submission file
file.write('Public Key: ' + str(pubkey) + '\n')

# close submission file
file.close()
