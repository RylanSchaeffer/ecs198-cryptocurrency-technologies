import rsa


def main():
    message = "I, Raymund Alksninis, signed this sentence!"
    message_enc = message.encode('utf-8')
    (publicKey, privateKey) = rsa.newkeys(1024)
    signature = rsa.sign(message_enc, privateKey, 'SHA-256')

    return(message, signature, publicKey)


