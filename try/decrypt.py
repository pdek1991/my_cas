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

def decrypt_string(key, encrypted_data):
    block_size = 16

    # Generate the same initialization vector (IV) used during encryption
    iv = pyaes.Counter(initial_value=0)

    # Create an AES cipher object with the provided key and CTR mode
    cipher = pyaes.AESModeOfOperationCTR(key.encode('utf-8'), counter=iv)

    # Decode the base64-encoded ciphertext
    ciphertext = base64.b64decode(encrypted_data)

    # Decrypt the ciphertext
    padded_plaintext = cipher.decrypt(ciphertext).decode('utf-8')

    # Remove the padding from the plaintext
    padding_length = ord(padded_plaintext[-1])
    plaintext = padded_plaintext[:-padding_length]
    return plaintext

key = "qwertyuioplkjhgf"
plaintext = "Hello, World!"

encrypted_data = encrypt_string(key, plaintext)
print("Encrypted data:", encrypted_data)

decrypted_data = decrypt_string(key, encrypted_data)
print("Decrypted data:", decrypted_data)

