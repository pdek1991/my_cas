import pyaes
import base64

def encrypt_string(key, plaintext):
    block_size = 16

    # Generate a random initialization vector (IV)
    iv = pyaes.Counter(initial_value=0)

    # Create an AES cipher object with the provided key and CTR mode
    cipher = pyaes.AESModeOfOperationCTR(key.encode('utf-8'), counter=iv)

    # Pad the plaintext to a multiple of the block size
    padding_length = block_size - (len(plaintext) % block_size)
    padded_plaintext = plaintext + padding_length * chr(padding_length)

    # Encrypt the padded plaintext
    ciphertext = cipher.encrypt(padded_plaintext.encode('utf-8'))

    # Encode the ciphertext in base64 for representation
    encrypted_data = base64.b64encode(ciphertext).decode('utf-8')

    return encrypted_data

# Example usage
key = 'ThisIsASecretKey'
plaintext = '7010004993:7010004993:10:2037-12-31'

encrypted_string = encrypt_string(key, plaintext)
print("Encrypted string:", encrypted_string)