import socket as so

def caesar_cipher(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text


client_socket=so.socket(so.AF_INET,so.SOCK_STREAM)
print ("Socket successfully created from client side")
server_address=('127.0.0.1',9999)
client_socket.connect(server_address)
data = client_socket.recv(1024).decode()
print ("Received:", data)
data= caesar_cipher(data,3)
print("Received:", data)
client_socket.close()