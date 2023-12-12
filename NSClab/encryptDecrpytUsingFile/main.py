from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization

# Read the private key from privatekey.pem
with open("privatekey.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None
    )

# Read the public key from publickey.pem
with open("publickey.pem", "rb") as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read()
    )

# Encrypt the message using the public key
message = "Hello, World!"
encrypted_message = public_key.encrypt(
    message.encode(),
    padding.PKCS1v15()
)

# Decrypt the encrypted message using the private key
decrypted_message = private_key.decrypt(
    encrypted_message,
    padding.PKCS1v15()
)

print("Original Message:", message)
print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message.decode())