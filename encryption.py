# --------------------------------------------------------------------------------------------------------
#                                         IMPORTING LIBRARIES 

# IMPORTS FOR ENCRYPTION TECHNIQUE 1
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# IMPORT FOR ENCRYPTION TECHNIQUE 2 - Fernet Encryption (OR, Symmetric Enryption)
from cryptography.fernet import Fernet

import os

# --------------------------------------------------------------------------------------------------------
#                                       AES, CBC Encyption
#                                           TECHNIQUE 1 

# Key generation function
def generate_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())
    return key

# Function to encrypt a file
def encrypt_file(file_path: str, password: str):
    salt = os.urandom(16)  # Generate a random salt
    key = generate_key(password, salt)
    iv = os.urandom(16)  # Generate a random IV

    # Read the file content
    with open(file_path, 'rb') as f:
        file_data = f.read()

    # Pad the file data
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(file_data) + padder.finalize()

    # Encrypt the data
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    # Write the encrypted data to a new file
    with open(file_path + '.enc', 'wb') as f:
        f.write(salt + iv + encrypted_data)

# Function to decrypt a file
def decrypt_file(file_path: str, password: str):
    with open(file_path, 'rb') as f:
        salt = f.read(16)  # Read the salt
        iv = f.read(16)  # Read the IV
        encrypted_data = f.read()  # Read the encrypted data

    key = generate_key(password, salt)

    # Decrypt the data
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(encrypted_data) + decryptor.finalize()

    # Unpad the data
    unpadder = padding.PKCS7(128).unpadder()
    file_data = unpadder.update(padded_data) + unpadder.finalize()

    # Write the decrypted data to a new file
    with open(file_path[:-4], 'wb') as f:
        f.write(file_data)
        
# Example usage

# Encrypt
# file_path = 'example.txt'
# password = 'my_secure_password'
# encrypt_file(file_path, password)

# Decrypt
# encrypted_file_path = 'example.txt.enc'
# password = 'my_secure_password'
# decrypt_file(encrypted_file_path, password)

# --------------------------------------------------------------------------------------------------------
#                                       Fernet Encryption
#                                          TECHNIQUE 2

# Generate a key for encryption
def generate_key_fernet():
    return Fernet.generate_key()

# Function to encrypt a file
def encrypt_file_fernet(file_path: str, key: bytes):
    with open(file_path, 'rb') as file:
        file_data = file.read()

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(file_data)

    encrypted_file_path = file_path + '.enc'
    with open(encrypted_file_path, 'wb') as file:
        file.write(encrypted_data)
    
    return encrypted_file_path

def encrypt_file_fernet_start(file_path, toEncrypt):
    key = generate_key_fernet()
    with open('filekey.key', 'wb') as key_file:
            key_file.write(key)
    if(toEncrypt == True):
        encrypted_file_path = encrypt_file_fernet(file_path, key)
        print(f'Encrypted file saved to: {encrypted_file_path}')
        return encrypted_file_path
    else:
        return key
    
# Function to load the key
def load_key():
    return open('filekey.key', 'rb').read()

# Function to decrypt a file
def decrypt_file_fernet(file_path: str, key: bytes):
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()

    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)

    decrypted_file_path = file_path[:-4]  # Remove the .enc extension
    with open(decrypted_file_path, 'wb') as file:
        file.write(decrypted_data)
    
    return decrypted_file_path

# Load the key
def decrypt_file_fernet_start(encrypted_file_path):
    key = load_key()
    decrypted_file_path = decrypt_file_fernet(encrypted_file_path, key)
    print(f'Decrypted file saved to: {decrypted_file_path}')


# Example usage

# Encrypt
# file_path = 'example.txt'
# encrypt_file_fernet_start(file_path, True)

# Decrypt
# encrypted_file_path = "example.txt.enc"
# decrypt_file_fernet_start(encrypted_file_path)

# --------------------------------------------------------------------------------------------------------