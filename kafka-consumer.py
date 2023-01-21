from kafka import KafkaConsumer
import sys
bootstrap_servers = ['localhost:9092']
topicName = 'third_topic'
consumer = KafkaConsumer (topicName, group_id = 'my-third-consumer-group',bootstrap_servers = bootstrap_servers,
auto_offset_reset = 'earliest')

try:
    for message in consumer:
        print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,message.offset, message.key,message.value))
except KeyboardInterrupt:
    sys.exit()