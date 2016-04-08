import rsa


def main():

    (my_pubkey, my_privkey) = rsa.newkeys(1024)
    message = 'I, Bryan Ngo, signed this message'.encode('utf-8')
    sign = rsa.sign(message, my_privkey, "SHA-256")
    rsa.verify(message, sign, my_pubkey)
    return message, sign, my_pubkey

main()
