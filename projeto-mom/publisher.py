import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='fila_exemplo')

channel.basic_publish(exchange='',
                      routing_key='fila_exemplo',
                      body='Mensagem de exemplo')

print("Mensagem enviada")
connection.close()
