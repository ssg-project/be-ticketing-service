from aiokafka import AIOKafkaProducer
import json
import asyncio
from ..config.config import KAFKA_BROKER_URL, KAFKA_TOPIC

class TicketService:
    def __init__(self):
        self.kafka_producer = AIOKafkaProducer(bootstrap_servers=KAFKA_BROKER_URL)
        
    async def reserve_ticket(self, user_id: int, concert_id: int):
        # Kafka로 티켓 예약 이벤트 발행
        await self.publish_ticket_event(user_id, concert_id)
        return "Ticket reserved successfully!"
        
    async def publish_ticket_event(self, user_id: int, concert_id: int):
        # Kafka에 티켓 예약 이벤트를 발행
        message = {
            "user_id": str(user_id),
            "concert_id": str(concert_id)
        }

        await self.kafka_producer.start()

        try:
            # Kafka에 티켓 예약 이벤트를 비동기적으로 발행
            await self.kafka_producer.send(KAFKA_TOPIC, json.dumps(message).encode('utf-8'))
            print("Message sent successfully")
        except Exception as e:
            print(f"Error sending message: {e}")
        finally:
            # 메시지 발송 후 프로듀서 종료
            await self.kafka_producer.stop()