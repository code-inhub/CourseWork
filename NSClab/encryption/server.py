import socket as so


def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text


server_socket=so.socket()
print ("Socket successfully created")
server_address=('127.0.0.1',9999)
server_socket.bind(server_address)
server_socket.listen(5)
while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")
    message = caesar_cipher("Hi I am Anshul",3)
    client_socket.send(message.encode())
    client_socket.close()