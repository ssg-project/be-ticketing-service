import os
from dotenv import load_dotenv

if not os.getenv("APP_ENV"):
    load_dotenv()

# Kafka 설정
KAFKA_BROKER_URL = os.getenv("KAFKA_BROKER_URL")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC")
KAFKA_GROUP_ID = os.getenv("KAFKA_GROUP_ID")