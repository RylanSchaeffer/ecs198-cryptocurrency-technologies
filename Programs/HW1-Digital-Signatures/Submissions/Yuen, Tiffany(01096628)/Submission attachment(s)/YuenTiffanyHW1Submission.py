import rsa
def main():
    (publicKey, privateKey) = rsa.newkeys(1024)
    msg = 'I, Tiffany Yuen, signed this sentence!'.encode('utf-8')
    signature = rsa.sign(msg, privateKey, 'SHA-256')
    return msg, signature, publicKey

if __name__ == '__main__':
    main()
