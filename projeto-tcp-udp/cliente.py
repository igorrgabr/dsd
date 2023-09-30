import socket
from game.imagem import exec_imagem

# configuração TCP
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_host = "localhost"
tcp_port = 1234
tcp_client_socket.connect((tcp_host, tcp_port))

# configuração UDP
udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_host = "localhost"
udp_port = 4321  # mesma porta definida no servidor UDP

# jogo
print('"Alea iacta est ou Alea jacta est."\n')
tcp_data = tcp_client_socket.recv(1024).decode()
frase_cifrada, desloc_romano = tcp_data.split(":")
print(frase_cifrada)
print(desloc_romano)
    
venceu = False
count = 0
while not venceu and count <= 5:
    tentativa = input("\ntuum conatus: ")

    # mensagem via TCP
    tcp_client_socket.send(tentativa.encode())
    tcp_data = tcp_client_socket.recv(1024)

    if tcp_data.decode() == "gratulationes":
        venceu = True
    
    print(f"\n{tcp_data.decode()}...\n")

    # dicas via UDP e imagens
    if venceu:
        exec_imagem(count, 1)
    elif count < 5:
        udp_client_socket.sendto(b"img", (udp_host, udp_port))
        tip, udp_server_address = udp_client_socket.recvfrom(1024)
        print(f"consilium {count+1} - {tip.decode()}\n")
        exec_imagem(count, 0)
    else:
        print("C. L. A. D. E. M.\n")
        exec_imagem(count, 2)

    count += 1

tcp_client_socket.close()
udp_client_socket.close()
