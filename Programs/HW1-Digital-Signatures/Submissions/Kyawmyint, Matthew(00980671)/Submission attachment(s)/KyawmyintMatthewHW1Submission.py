def main():
    import rsa
    message = "I, Matthew Kyawmyint, signed this sentence!".encode('utf-8')

    (matt_pub, matt_priv) = rsa.newkeys(1024)
    signature = rsa.sign(message, matt_priv, 'SHA-256')
    return message, signature, matt_priv
