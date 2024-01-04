import threading
import queue
import time

class Publisher:
    def __init__(self, fila_mensagens):
        self.fila_mensagens = fila_mensagens

    def enviar_mensagens(self):
        for i in range(5):
            mensagem = f"Mensagem {i}"
            self.fila_mensagens.put(mensagem)
            print(f"Produtor enviou: {mensagem}")
            time.sleep(1)

# Se estiver executando este arquivo individualmente
if __name__ == "__main__":
    fila_mensagens = queue.Queue()
    publisher = Publisher(fila_mensagens)
    publisher.enviar_mensagens()
