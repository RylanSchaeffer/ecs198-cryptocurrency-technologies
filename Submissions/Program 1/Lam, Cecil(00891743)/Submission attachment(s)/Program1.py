import rsa

def main():
	(pubkey, privkey) = rsa.newkeys(512)
	test = "goob"
	signature = rsa.sign(test, privkey, 'SHA-1')
	msg = ("I, Cecil Lam, signed this sentence!")
	publicKey = pubkey
	return msg, signature, publicKey;

print(main())
