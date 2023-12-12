import socket
import random

# Server configuration
host = '127.0.0.1'  # Loopback address (localhost)
port = 12345       # Port to connect to

# Shared prime number and base (publicly known)
p = 23  # Prime number
g = 5   # Primitive root modulo p

# Client's private key
client_private_key = random.randint(1, 10)

# Calculate the client's public key
client_public_key = (g ** client_private_key) % p

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((host, port))

# Receive the server's public key
server_public_key = int(client_socket.recv(1024).decode('utf-8'))
print(f"Received Server's Public Key: {server_public_key}")

# Send the client's public key to the server
client_socket.send(str(client_public_key).encode('utf-8'))

# Calculate the shared secret key
shared_secret_key = (server_public_key ** client_private_key) % p
print(f"Shared Secret Key: {shared_secret_key}")

while True:
    # Get user input for the message to send
    message = input("Enter a message (or 'exit' to quit): ")
    
    if message == 'exit':
        break
    
    # Encrypt the message using the shared secret key (simple XOR for demonstration)
    encrypted_message = ''.join([chr(ord(c) ^ shared_secret_key) for c in message])
    client_socket.send(encrypted_message.encode('utf-8'))

    # Receive a response from the server (encrypted)
    encrypted_response = client_socket.recv(1024).decode('utf-8')
    
    # Decrypt the response using the shared secret key (simple XOR for demonstration)
    decrypted_response = ''.join([chr(ord(c) ^ shared_secret_key) for c in encrypted_response])
    print(f"Received from server (encrypted): {encrypted_response}")
    print(f"Decrypted response: {decrypted_response}")

# Close the connection
client_socket.close()
