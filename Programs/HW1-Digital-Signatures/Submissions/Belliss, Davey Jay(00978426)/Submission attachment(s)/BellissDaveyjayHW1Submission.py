import rsa
def main():
  message =  "I, Davey Jay Belliss, signed this sentence!"
  (pubkey, privkey) = rsa.newkeys(2048)
  signature = rsa.sign(message, privkey, 'SHA-256')
  DigSig =  signature
  PublicKey = pubkey

#  print message
#  print DigSig
#  print pubkey
#  print '\n'
#  print rsa.verify(message, signature, pubkey)
  return message, DigSig, PublicKey

if __name__ =="__main__": 
  main()
