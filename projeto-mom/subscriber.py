import pika
import json

cloudamqp_url = "amqps://gjmcunrj:dGqU85f85QKJF33Azx8voAmxBeM2Q8CY@jackal.rmq.cloudamqp.com/gjmcunrj"
params = pika.URLParameters(cloudamqp_url)
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.exchange_declare(exchange='leilao', exchange_type='fanout')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='leilao', queue=queue_name)

def callback(ch, method, properties, body):
    art = json.loads(body)
    print(f"Nova arte para leilão: {art['nome']}")

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

print('Aguardando novas artes para leilão.')
print('Para sair, Ctrl+C.')
channel.start_consuming()
