import socket
import random

def diffie_hellman_client():
    p = 23  # Prime number (commonly agreed upon)
    g = 5   # Generator (commonly agreed upon)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = "192.168.137.1"  # Replace with the server's IP address or hostname
    server_port = 12345

    client_socket.connect((server_address, server_port))

    # Client's secret key
    a_private_key = random.randint(1, p - 1)

    # Calculate client's public key
    a_public_key = (g ** a_private_key) % p

    # Send client's public key to the server
    client_socket.send(str(a_public_key).encode())

    # Receive server's public key
    server_public_key = int(client_socket.recv(1024).decode())

    # Calculate the shared secret
    shared_secret = (server_public_key ** a_private_key) % p

    print(f"Shared secret on the client: {shared_secret}")

    client_socket.close()


    diffie_hellman_client()