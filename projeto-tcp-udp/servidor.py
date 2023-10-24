import socket
import random
from game.criptografia import criptografar, descriptografar
from game.frase import frase_aleatoria
from game.romano import int_romano
from game.urls import *

# configuração TCP
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_host = "localhost"
tcp_port = 1234
tcp_server_socket.bind((tcp_host, tcp_port))
tcp_server_socket.listen()

# configuração UDP
udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_host = "localhost"
udp_port = 4321  # porta diferente para o UDP
udp_server_socket.bind((udp_host, udp_port))

# jogo
print("Cryptography...\n")
deslocamento = random.randint(1, 25)
desloc_romano = int_romano(deslocamento)
frase_cifrada = criptografar(frase_aleatoria(), deslocamento)
tcp_client_socket, tcp_client_address = tcp_server_socket.accept()
tcp_client_socket.send(f"{frase_cifrada}:{desloc_romano}".encode())

venceu = False
count = 0
while not venceu and count <= 5:
    # TCP
    tcp_data = tcp_client_socket.recv(1024)
    print(f"tentativa {count+1}: {tcp_data.decode()}")

    if tcp_data.decode() == descriptografar(frase_cifrada, deslocamento):
        venceu = True
        tcp_client_socket.send(b"gratulationes")
        print(f"venceu após {count+1} tentativa(s)...\n")
    else:
        tcp_client_socket.send(b"errare")
        print(f"tic, tac... restam {5-count} tentativa(s)." if 5 - count > 0 else "as chances acabaram.\n")
    
    # UDP
    udp_data, udp_server_address = udp_server_socket.recvfrom(1024)

    if udp_data.decode() == "img":
        if venceu:
            print("imagem de vitória enviada.\n")
            udp_server_socket.sendto(img_win_url.encode(), udp_server_address)
        elif count < 5:
            print(f"dica n°{count+1} enviada.\n")
            udp_server_socket.sendto(img_urls[count].encode(), udp_server_address)
        else:
            print("imagem de derrota enviada.\n")
            udp_server_socket.sendto(img_lose_url.encode(), udp_server_address)

    count += 1
    
print("...decryption.")
tcp_client_socket.close()
tcp_server_socket.close()
