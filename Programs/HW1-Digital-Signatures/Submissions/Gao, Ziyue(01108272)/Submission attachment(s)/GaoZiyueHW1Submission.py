import rsa
from rsa import key

def main():

    (publicKey, privateKey) = key.newkeys(1024)
    sentence = b'I, Ziyue Gao, signed this sentence!'
    sig = rsa.sign(sentence, privateKey, 'SHA-256')
    enc = rsa.encrypt(sentence, publicKey)
    return sentence, sig, publicKey