import socket as so
server_socket=so.socket()
print ("Socket successfully  created from server side")
server_address=('127.0.0.1',9999)
server_socket.bind(server_address)
server_socket.listen(2)
while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")
    message = "Welcome to the server Anshul!"
    client_socket.send(message.encode())
    client_socket.close()