import rsa

def main():
	(pub_key, priv_key) = rsa.newkeys(1024)
	message = 'I, Stephan Zharkov, signed this message!'.encode('ASCII')
	signature = rsa.sign(message, priv_key, 'SHA-256')

	return message, signature, pub_key


if __name__ == '__main__':
  main()
