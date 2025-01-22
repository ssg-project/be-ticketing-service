from kafka import KafkaProducer
import json, os

class KafkaTicketProducer:
    bootstrap_servers=os.getenv('BOOTSTRAP_HOST', 'localhost')
    def __init__(self, bootstrap_servers=[f'{bootstrap_servers}:9093']):
        self.producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda x: json.dumps(x).encode('utf-8')
        )

    def send_message(self, topic, message):
        self.producer.send(topic, value=message)
        self.producer.flush()