import os


# Kafka 설정
KAFKA_BROKER_URL = os.getenv("KAFKA_BROKER_URL", "localhost:9092")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "ticketing-reservation")
KAFKA_GROUP_ID = os.getenv("KAFKA_GROUP_ID", "reservation-group")