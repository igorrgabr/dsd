from flask import Flask, render_template
from threading import Thread
import pika
import json
import locale

app = Flask(__name__)

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

cloudamqp_url = "amqps://gjmcunrj:dGqU85f85QKJF33Azx8voAmxBeM2Q8CY@jackal.rmq.cloudamqp.com/gjmcunrj"
params = pika.URLParameters(cloudamqp_url)
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.exchange_declare(exchange='leilao', exchange_type='fanout')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='leilao', queue=queue_name)

arts_for_auction = []

def setup_rabbitmq():
    def callback(ch, method, properties, body):
        art = json.loads(body)
        arts_for_auction.append(art)
        print(f"Nova arte para leilão: {art['nome']}")
    
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    print('Aguardando novas artes para leilão.')
    print('Para sair, Ctrl+C.')
    channel.start_consuming()

@app.template_filter('format_money')
def format_money(valor):
    return locale.currency(valor, grouping=True)

@app.route('/')
def index():
    return render_template('index.html', arts=arts_for_auction, format_money=format_money)

if __name__ == '__main__':
    rabbitmq_thread = Thread(target=setup_rabbitmq)
    rabbitmq_thread.start()

    app.run(host='0.0.0.0', debug=True)
