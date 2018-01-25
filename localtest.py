from kafka import KafkaConsumer

TOPIC = 'maxwell'
SERVER = 'localhost'
PORT = '9093'		# manager port

MSG_LIMIT = 10

#consumer = KafkaConsumer(TOPIC)

consumer = KafkaConsumer(TOPIC, bootstrap_servers=':'.join([SERVER, PORT]))

for idx in range(10):
    msg = next(consumer)
    print(msg)
    print('\n')

