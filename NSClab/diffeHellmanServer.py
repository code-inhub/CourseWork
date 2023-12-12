
import socket
import random

def diffie_hellman_server():
    p = 23  # Prime number (commonly agreed upon)
    g = 5   # Generator (commonly agreed upon)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("", 12345))
    server_socket.listen(1)

    print("Server waiting for connection...")
    conn, addr = server_socket.accept()
    print(f"Connection from {addr}")

    # Server's secret key
    b_private_key = random.randint(1, p - 1)

    # Receive client's public key
    client_public_key = int(conn.recv(1024).decode())

    # Calculate server's public key
    b_public_key = (g ** b_private_key) % p

    # Send server's public key to the client
    conn.send(str(b_public_key).encode())

    # Calculate the shared secret
    shared_secret = (client_public_key ** b_private_key) % p

    print(f"Shared secret on the server: {shared_secret}")

    conn.close()
    server_socket.close()


    diffie_hellman_server()