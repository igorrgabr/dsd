import queue
import time

class Consumer:
    def __init__(self, fila_mensagens):
        self.fila_mensagens = fila_mensagens

    def processar_mensagens(self):
        while True:
            mensagem = self.fila_mensagens.get()
            print(f"Consumidor recebeu: {mensagem}")
            # Aqui você pode adicionar lógica para processar a mensagem
            time.sleep(2)
            self.fila_mensagens.task_done()

# Se estiver executando este arquivo individualmente
if __name__ == "__main__":
    fila_mensagens = queue.Queue()
    consumer = Consumer(fila_mensagens)
    consumer.processar_mensagens()
