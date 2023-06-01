import pyaes
import base64

def encrypt_string(key, plaintext):
    # Pad the plaintext to be a multiple of 16 bytes (required by AES)
    padded_plaintext = plaintext + (16 - len(plaintext) % 16) * chr(16 - len(plaintext) % 16)
    
    # Create an AES cipher object with the provided key
    cipher = pyaes.AESModeOfOperationECB(key.encode('utf-8'))
    
    # Encrypt the padded plaintext
    ciphertext = cipher.encrypt(padded_plaintext.encode('utf-8'))
    
    # Encode the ciphertext in base64 for better representation
    encrypted_data = base64.b64encode(ciphertext).decode('utf-8')
    
    return encrypted_data

# Example usage
key = 'qwertyuioplkjhgd'
plaintext = 'Hello, World!'

encrypted_string = encrypt_string(key, plaintext)
print("Encrypted string:", encrypted_string)


def decrypt_string(key, encrypted_data):
    # Decode the base64 encoded ciphertext
    ciphertext = base64.b64decode(encrypted_data)
    
    # Create an AES cipher object with the provided key
    cipher = pyaes.AESModeOfOperationECB(key.encode('utf-8'))
    
    # Decrypt the ciphertext
    decrypted_data = cipher.decrypt(ciphertext).decode('utf-8')
    
    # Remove the PKCS7 padding from the decrypted data
    padding_length = ord(decrypted_data[-1])
    decrypted_data = decrypted_data[:-padding_length]
    
    return decrypted_data

# Example usage
key = 'qwertyuioplkjhgd'
#encrypted_string = 'WzFGzW6iB6YlwfbFQgYF6A=='

decrypted_string = decrypt_string(key, encrypted_string)
print("Decrypted string:", decrypted_string)