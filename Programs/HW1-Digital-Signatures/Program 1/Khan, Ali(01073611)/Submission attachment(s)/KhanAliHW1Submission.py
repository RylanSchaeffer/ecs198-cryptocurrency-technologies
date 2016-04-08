import Crypto
from Crypto.PublicKey import RSA

message = "I, Ali Khan, signed this sentence!"
privateKey = RSA.generate(1024)
publicKey = privateKey.publickey()

def main():
	return(message, privateKey, publicKey)
    

if __name__ == '__main__':
    main()
               




