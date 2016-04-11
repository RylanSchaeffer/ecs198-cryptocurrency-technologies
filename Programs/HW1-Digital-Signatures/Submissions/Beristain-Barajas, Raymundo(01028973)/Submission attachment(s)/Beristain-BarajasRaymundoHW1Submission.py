import rsa

def main():
    (pubkey, privkey) = rsa.newkeys(1024)
    msg = "I, Raymundo, signed this sentence!"
    signature = rsa.sign(msg.encode('utf-8'), privkey, 'SHA-256')

    return msg, signature, pubkey
if __name__ == '__main__':
    main()
