import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"  # Endereço IP do servidor
port = 12345       # Porta do servidor

client_socket.connect((host, port))

client_socket.send(b"Olá, servidor!")  # Envia dados para o servidor
data = client_socket.recv(1024)  # Recebe dados do servidor

client_socket.close()
