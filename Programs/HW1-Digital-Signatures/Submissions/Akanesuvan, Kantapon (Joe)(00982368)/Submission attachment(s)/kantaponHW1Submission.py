import rsa

def main():
  msg = "I Kantapon (Joe) Akanesuvan, signed this sentence!"
  (publicKey, privKey) = rsa.newkeys(1024)
  signature = rsa.sign(msg, privKey, 'SHA-256')
  return (msg, signature, publicKey)

