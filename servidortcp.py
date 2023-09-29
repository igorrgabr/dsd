import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"  # Endereço IP do servidor
port = 12345       # Porta do servidor

server_socket.bind((host, port))
server_socket.listen()

print(f"Servidor TCP está ouvindo em {host}:{port}")

client_socket, client_address = server_socket.accept() # Aceita conexão de clientes
data = client_socket.recv(1024)  # Recebe dados do cliente
client_socket.send(b"Obrigado por se conectar!")  # Envia dados para o cliente

client_socket.close()
server_socket.close()
