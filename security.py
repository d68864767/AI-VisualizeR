```python
# Import necessary libraries
from cryptography.fernet import Fernet
import os

# Generate a key for encryption and decryption
# You must save this key or once lost you will no longer be able to decrypt data that was encrypted with this key.
# The fernet guarantees that a message encrypted using it cannot be manipulated or read without the key.
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def secure_data(data):
    """
    This function takes raw data as input and performs data security steps such as encryption.
    """

    # Convert data to string format
    data_str = str(data)

    # Encrypt the data
    encrypted_data = encrypt_data(data_str)

    return encrypted_data

def encrypt_data(data_str):
    """
    This function takes a string as input and performs data encryption.
    """

    # Encode the data
    data_bytes = data_str.encode('utf-8')

    # Encrypt the data
    encrypted_data = cipher_suite.encrypt(data_bytes)

    return encrypted_data

def decrypt_data(encrypted_data):
    """
    This function takes encrypted data as input and performs data decryption.
    """

    # Decrypt the data
    decrypted_data = cipher_suite.decrypt(encrypted_data)

    # Decode the data
    data_str = decrypted_data.decode('utf-8')

    return data_str
```
