import socket

# configuração TCP
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_host = "localhost"
tcp_port = 1234
tcp_client_socket.connect((tcp_host, tcp_port))

# configuração UDP
udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_host = "localhost"
udp_port = 4321  # mesma porta definida no servidor UDP

venceu = False
while not venceu:
    mensagem = input("Digite sua mensagem: ")

    # mensagem via TCP
    tcp_client_socket.send(mensagem.encode())
    tcp_data = tcp_client_socket.recv(1024)
    print("Resposta do servidor (TCP):", tcp_data.decode())

    # mensagem via UDP
    udp_client_socket.sendto(mensagem.encode(), (udp_host, udp_port))
    print("Mensagem enviada via UDP.")

tcp_client_socket.close()
udp_client_socket.close()
