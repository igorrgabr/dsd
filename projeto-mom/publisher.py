import pika
import json

cloudamqp_url = "amqps://gjmcunrj:dGqU85f85QKJF33Azx8voAmxBeM2Q8CY@jackal.rmq.cloudamqp.com/gjmcunrj"
params = pika.URLParameters(cloudamqp_url)
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.exchange_declare(exchange='leilao', exchange_type='fanout')

def publish_new_art():
    nome = input("Nome da arte: ")
    imagem = input("URL da imagem: ")
    valor_inicial = float(input("Valor inicial: "))

    nova_arte = {"nome": nome, "img": imagem, "valor_inicial": valor_inicial}
    message = json.dumps(nova_arte)

    channel.basic_publish(exchange='leilao', routing_key='', body=message)
    print(f"Nova arte '{nome}' publicada para leilão")

if __name__ == "__main__":
    while True:
        user_choice = input("Deseja publicar uma nova arte? (s/n): ").lower()
        if user_choice != 's':
            break

        publish_new_art()

    connection.close()
