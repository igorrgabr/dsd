import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = "127.0.0.1"  # Endereço IP do servidor
port = 12345       # Porta do servidor

server_socket.bind((host, port))

print(f"Servidor UDP está ouvindo em {host}:{port}")

data, client_address = server_socket.recvfrom(1024)  # Recebe dados do cliente

server_socket.sendto(b"Obrigado por se conectar!", client_address)

server_socket.close()
