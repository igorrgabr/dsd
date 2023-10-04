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

    # dicas e imagens via UDP
    udp_client_socket.sendto(b"img", (udp_host, udp_port))
    tip_url, udp_server_address = udp_client_socket.recvfrom(1024)
    
    if venceu:
        nome = "vincere.png"
    elif count < 5:
        nome = f"imago{count+1}.png"
    else:
        nome = "victus.png"
        print("C. L. A. D. E. M.\n")

    if tip_url:
        exec_imagem(tip_url.decode(), nome)

    count += 1

tcp_client_socket.close()
udp_client_socket.close()
