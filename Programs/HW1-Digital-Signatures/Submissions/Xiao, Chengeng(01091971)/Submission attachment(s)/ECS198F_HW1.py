import rsa
from rsa import key
def main():
    (pub_key, priv_key) = key.newkeys(1024)
    raw = b'I, Chengeng Xiao, signed this sentence!'
    crypto = rsa.encrypt(raw, pub_key)
    signature = rsa.sign(raw, priv_key, 'SHA-256')
    msg = rsa.decrypt(crypto, priv_key)
    return msg, signature, pub_key

msg, digsig, pkey = main()
print('msg: ', msg)
print('signature: ', digsig)
print('publickey: ', pkey)