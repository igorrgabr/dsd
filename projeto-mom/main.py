import threading
from publisher import Publisher
from consumer import Consumer
import queue

# Se estiver executando este arquivo individualmente
if __name__ == "__main__":
    fila_mensagens = queue.Queue()

    # Criar instâncias do produtor e consumidor
    publisher = Publisher(fila_mensagens)
    consumer = Consumer(fila_mensagens)

    # Criar threads para o produtor e consumidor
    thread_produtor = threading.Thread(target=publisher.enviar_mensagens)
    thread_consumidor = threading.Thread(target=consumer.processar_mensagens)

    # Iniciar as threads
    thread_produtor.start()
    thread_consumidor.start()

    # Aguardar até que todas as mensagens sejam processadas
    fila_mensagens.join()

    # Aguardar as threads terminarem
    thread_produtor.join()
    thread_consumidor.join()
