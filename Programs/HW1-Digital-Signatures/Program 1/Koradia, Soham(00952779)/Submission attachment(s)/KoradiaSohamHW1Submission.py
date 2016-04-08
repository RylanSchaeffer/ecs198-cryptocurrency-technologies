'''
Name: Soham Koradia
Class: ECS 198F: Cryptocurrency in Python
HW Assignment: 1
'''

# Import the rsa module in order to sign the message
import rsa

def main():
    # Initialize the message
    message = 'I, Soham, signed this sentence!'

    # Use UTF-8 encoding on the message in order for it to be hashed correctly
    message = message.encode('utf-8')

    # First generate a public and private key pair
    publicKey, privateKey = rsa.newkeys(2048)

    # Now sign the message using the rsa library's sign method, using the 'SHA-1' hash method
    signatureOfMessage = rsa.sign(message, privateKey, 'SHA-256')

    # Now return the public key and signature for someone to decrypt and verify that it was actually me who sent it
    return message, signatureOfMessage, publicKey

# Uncomment if wanting to run the main method without explicitly calling it 
# main()
