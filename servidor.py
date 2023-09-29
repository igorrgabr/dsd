import socket
import random
from game.cifra import criptografar
from game.frase import frase_aleatoria
from game.romano import int_romano

# configuração TCP
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_host = "localhost"
tcp_port = 1234
tcp_server_socket.bind((tcp_host, tcp_port))
tcp_server_socket.listen()
print(f"Servidor TCP está ouvindo em {tcp_host}:{tcp_port}")

# configuração UDP
udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_host = "localhost"
udp_port = 4321  # porta diferente para o UDP
udp_server_socket.bind((udp_host, udp_port))
print(f"Servidor UDP está ouvindo em {udp_host}:{udp_port}")

# jogo
print("J ogo da C riptografia")
print("Alea iacta est ou Alea jacta est.")

deslocamento = random.randint(1, 25)
print(int_romano(deslocamento))

frase = frase_aleatoria()
p1 = criptografar(frase[0], deslocamento)
p2 = criptografar(frase[1], deslocamento)
p3 = criptografar(frase[2], deslocamento)

venceu = False

while not venceu:
    # conexões TCP
    tcp_client_socket, tcp_client_address = tcp_server_socket.accept()
    tcp_data = tcp_client_socket.recv(1024)

    # processamento de mensagens TCP
    tcp_client_socket.send(b"Obrigado por se conectar via TCP!")
    tcp_client_socket.close()

    # lidar com mensagens UDP
    udp_data, udp_client_address = udp_server_socket.recvfrom(1024)

    # processamento de mensagens UDP
    