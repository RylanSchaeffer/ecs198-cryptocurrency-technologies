import rsa

def main():
    message = 'I, Tobias, signed this sentence!'
    (pubkey, privkey) = rsa.newkeys(1024)
    signature = rsa.sign(message, privkey, 'SHA-256')
    return message, signature, pubkey
        
if __name__ == '__main__':
    main()