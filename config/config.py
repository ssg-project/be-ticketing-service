import os
from dotenv import load_dotenv
import boto3
import json
from botocore.exceptions import ClientError

if not os.getenv("APP_ENV"):
    load_dotenv()

    # Kafka 설정
    KAFKA_BROKER_URL = os.getenv("KAFKA_BROKER_URL")
    KAFKA_TOPIC = os.getenv("KAFKA_TOPIC")
    KAFKA_GROUP_ID = os.getenv("KAFKA_GROUP_ID")

else:
    secret_name = "secret/ticketing/ticketing"
    region_name = "ap-northeast-2"

    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        raise e

    secret = get_secret_value_response['SecretString']
    
    secret_data = json.loads(secret)

    KAFKA_BROKER_URL = secret_data["KAFKA_BROKER_URL"]
    KAFKA_TOPIC = secret_data["KAFKA_TOPIC"]
    KAFKA_GROUP_ID = secret_data["KAFKA_GROUP_ID"]