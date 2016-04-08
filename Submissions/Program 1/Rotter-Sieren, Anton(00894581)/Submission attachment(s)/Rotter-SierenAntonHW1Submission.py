import rsa
def main():
    message = "I, Anton Rotter-Sieren, signed this sentence!".encode('utf-8')
    (pubkey, privkey) = rsa.newkeys(1048)
    signature = rsa.sign(message, privkey, 'SHA-256')
    return message,signature,pubkey

main()