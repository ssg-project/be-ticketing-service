from kafka import KafkaProducer
import json

class KafkaTicketProducer:
    def __init__(self, bootstrap_servers=['localhost:9093']):
        self.producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda x: json.dumps(x).encode('utf-8')
        )

    def send_message(self, topic, message):
        self.producer.send(topic, value=message)
        self.producer.flush()