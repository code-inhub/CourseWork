import socket as so
client_socket=so.socket(so.AF_INET,so.SOCK_STREAM)
print ("Socket successfully created from client side")
server_address=('127.0.0.1',9999)
client_socket.connect(server_address)
data = client_socket.recv(1024).decode()
print("Received:", data)
client_socket.close()