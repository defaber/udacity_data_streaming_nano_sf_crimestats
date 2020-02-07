import asyncio

from confluent_kafka import Consumer
from confluent_kafka.admin import AdminClient, NewTopic

BROKER_URL = 'PLAINTEXT://localhost:9092'
TOPIC_NAME = 'com.udacity.sf.crimestats'

async def consume(topic_name):
    consumer = Consumer({
        'bootstrap.servers': BROKER_URL,
        'group.id': '0',
    })
    
    consumer.subscribe([topic_name])
    
    while True:
        messages = consumer.consume(5, timeout=1)
        
        for message in messages:
            if message is None:
                print('Message not found')
            elif message.error() is not None:
                print(f'Error: {message.error()}')
            else:
                print(f'{message.value()}\n')
                
        await asyncio.sleep(1)
                
def main():
    try:
        asyncio.run(consume(TOPIC_NAME))
        
    except KeyboardInterrupt as e:
        print("Shutting down...")
        
if __name__ == '__main__':
    main()
