import rsa


def main():
    message = "I, Annie, signed this sentence!".encode('utf-8')
    (pubkey, privkey) = rsa.newkeys(1024, poolsize=8)
    sign = rsa.sign(message, privkey, 'SHA-256')

    print(message, sign, pubkey)


if __name__ == "__main__":
    main()
