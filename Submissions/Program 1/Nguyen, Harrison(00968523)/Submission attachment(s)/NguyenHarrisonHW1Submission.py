import rsa

def main():
    (pubkey, privkey) = rsa.newkeys(1024)
    msg = "I, Harrison Nguyen, signed this sentence".encode('utf-8')
    signature = rsa.sign(msg, privkey, "SHA-256")
    rsa.verify(msg, signature, pubkey)
    return msg, signature, pubkey

main()