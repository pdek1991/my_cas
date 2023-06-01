from confluent_kafka import Consumer, KafkaException

# Configure consumer properties
consumer_config = {
    'bootstrap.servers': '192.168.56.112:9092',
    'group.id': 'emmg',
    'auto.offset.reset': 'earliest'
}

# Create a Kafka consumer instance
consumer = Consumer(consumer_config)

# Subscribe to the topic
consumer.subscribe(['topic_mycas'])

# Consume messages
while True:
    try:
        msg = consumer.poll(1.0)  # Wait for 1 second for a message
        if msg is None:
            continue
        elif not msg.error():
            # Process the message
            print(f"Received message: {msg.value().decode('utf-8')}")

            # Commit the message offset
            consumer.commit(msg)
        elif msg.error().code() == KafkaException._PARTITION_EOF:
            # Reached the end of a partition
            print(f"Reached end of partition {msg.topic()}-{msg.partition()}")
        else:
            # Handle other error cases
            print(f"Error: {msg.error().str()}")
    except KeyboardInterrupt:
        break

# Close the consumer
consumer.close()
