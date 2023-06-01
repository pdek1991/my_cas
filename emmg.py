#from Crypto.Cipher import AES
from datetime import datetime
from confluent_kafka import Consumer, KafkaException, KafkaError
import mysql.connector
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend




conf = {
    'bootstrap.servers': '192.168.56.112:9092',
    'group.id': 'emmg',
    'auto.offset.reset': 'earliest'
}

mysql_host = '192.168.56.112'
mysql_user = 'omi_user'
mysql_password = 'omi_user'
mysql_database = 'cas'

aes_key = b'abcdefghijklmnop'
aes_iv = b'1234567890abcdef'

# Create Kafka consumer
consumer = Consumer(conf)

# Subscribe to the topic
topic = 'topic_mycas'
consumer.subscribe([topic])

mysql_connection = mysql.connector.connect(
    host=mysql_host,
    user=mysql_user,
    password=mysql_password,
    database=mysql_database
)
mysql_cursor = mysql_connection.cursor()

def encrypt_message(message, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt

try:
    while True:
        # Poll for messages
        msg = consumer.poll(timeout=1.0)

        if msg is None:
            continue
        elif msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                # Reached end of partition, continue to next partition
                continue
            else:
                # Handle other errors
                print(f"Error: {msg.error().str()}")
                break
        else:
            # Process the message
            #encrypted_data = encrypt_message(msg.value(), aes_key, aes_iv)
            encrypted_data = msg.value()
            start_time = int(datetime.now().timestamp())

            # Parse the last column of the message to extract the date
            last_column = msg.value().decode('utf-8').split(':')[-1].strip()
            date_obj = datetime.strptime(last_column, '%Y-%m-%d')
            end_time = int(date_obj.replace(hour=0, minute=0, second=0).timestamp())
            emmtype = msg.value().decode('utf-8').split(':')[-2].strip()
            # Save the encrypted data, start time, end time, and other required information to the database
            insert_query = "INSERT INTO emmg (starttime, endtime, emmdata, emmtype) VALUES (%s, %s, %s, %s)"
            data = (start_time, end_time, encrypted_data, emmtype)
            mysql_cursor.execute(insert_query, data)
            mysql_connection.commit()

except KeyboardInterrupt:
    # Stop consuming when interrupted
    pass

finally:
    # Close the consumer and MySQL connection to release resources
    consumer.close()
    mysql_cursor.close()
    mysql_connection.close()

# AES encryption function
#def encrypt_message(message, key, iv):
 #   cipher = AES.new(key, AES.MODE_CBC, iv)
  #  ciphertext = cipher.encrypt

def encrypt_message(message, key, iv):
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(message) + encryptor.finalize()
    return encrypted_data