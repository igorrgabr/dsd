import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = "127.0.0.1"  # Endereço IP do servidor
port = 12345       # Porta do servidor

client_socket.sendto(b"Olá, servidor!", (host, port))

data, server_address = client_socket.recvfrom(1024)  # Recebe dados do servidor

client_socket.close()
