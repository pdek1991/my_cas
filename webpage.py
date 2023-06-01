
from flask import Flask, request
import mysql.connector.pooling
import logging
from logging.handlers import TimedRotatingFileHandler
from confluent_kafka import Consumer, KafkaException
from kafka.errors import KafkaError
from kafka import KafkaProducer
from flask import Flask, render_template, request, flash, redirect, get_flashed_messages
from flask.helpers import url_for
import json
import os.path
if not os.path.exists(r'.\Logs'):
    os.makedirs(r'.\Logs')



bootstrap_servers = '192.168.56.112:9092'
producer = KafkaProducer(bootstrap_servers=bootstrap_servers)


app = Flask(__name__)
app.secret_key = 'pdek1991'
app.debug = True
#app.logger.disabled = True


logging.basicConfig(format='%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s', datefmt='%d-%m-%Y:%H:%M:%S', level=logging.DEBUG,
                        handlers=[TimedRotatingFileHandler(filename=r'.\Logs\mycas.txt', backupCount=10, when='midnight', interval=1)])
logger = logging.getLogger(__name__)

flask_logger = logging.getLogger('werkzeug')
flask_logger.setLevel(logging.ERROR)

internal_logger = logging.getLogger('werkzeug._internal')
internal_logger.setLevel(logging.ERROR)

kafka_logger = logging.getLogger('kafka')
kafka_logger.setLevel(logging.INFO)

# Create a connection pool
db_config = {
    "host": "192.168.56.112",
    "user": "omi_user",
    "password": "omi_user",
    "database": "cas",
}

connection_pool = mysql.connector.pooling.MySQLConnectionPool(pool_name="my_pool", pool_size=10, **db_config)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
@app.route('/generate_osm', methods=['GET', 'POST'])
def generate_osm():
    message_id = request.form['message_id']
    message_text = request.form['message_text']
    device_id = request.form['device_id']
    expiry = request.form['expiry']
    topic = 'topic_mycas' 
    emmtype = '44'
    message = f'{device_id}:{message_id}:{message_text}:{emmtype}:{expiry}'
    try:
        producer.send(topic, message.encode('utf-8')).get()
        logger.info(f"Message sent to Kafka topic {topic}: {message}")
    except KafkaError as e:
        logger.error(f"Failed to send message to Kafka: {e}")
    # Acquire a connection from the pool
    connection = connection_pool.get_connection()

    # Execute the query using the acquired connection
    cursor = connection.cursor()
    insert_query = "INSERT INTO generate_osm (message_id, message_text, device_id, expiry) VALUES (%s, %s, %s, %s)"
    data = (message_id, message_text, device_id, expiry)
    cursor.execute(insert_query, data)
    connection.commit()
    logger.info((f"message_id: %s, message_text: %s, device_id: %s, expiry: %s" %(message_id, message_text, device_id, expiry)))
    # Release the connection back to the pool
    cursor.close()
    connection.close()
    flash('Message sent successfully!', 'success')
    flash_messages = json.dumps(dict(get_flashed_messages(with_categories=True)))
    return render_template('index.html', flash_messages=flash_messages)
    #return 'Message saved successfully', 200

@app.route('/addentitlement', methods=['GET', 'POST'])
def add_entitlement():
    device_id = request.form['device_id']
    package_ids = request.form['package_ids'].split(":")
    expiry = request.form['expiry']
    topic = 'topic_mycas'  # Replace with your Kafka topic name
    emmtype = '21'
    # Acquire a connection from the pool
    connection = connection_pool.get_connection()

    # Execute the query using the acquired connection
    cursor = connection.cursor()
    insert_query = "INSERT INTO entitlements (device_id, package_id, expiry) VALUES (%s, %s, %s)"
    for package_id in package_ids:
        data = (device_id, package_id, expiry)
        cursor.execute(insert_query, data)
        message = f'{device_id}:{package_id}:{emmtype}:{expiry}'
        try:
            producer.send(topic, message.encode('utf-8')).get()
            logger.info(f"Message sent to Kafka topic {topic}:{message}:{expiry}")
        except KafkaError as e:
            logger.error(f"Failed to send message to Kafka: {e}")
        logger.info((f"device_id: %s, package_id: %s, expiry: %s" %(device_id, package_id, expiry)))
    connection.commit()
    # Release the connection back to the pool
    cursor.close()
    connection.close()
    flash('Entitlement added successfully!', 'success')
    flash_messages = json.dumps(dict(get_flashed_messages(with_categories=True)))
    return render_template('index.html', flash_messages=flash_messages)
   
@app.route('/device_keys', methods=['GET', 'POST'])
def device_keys():
    device_id = request.form['device_id']
    bskeys = request.form['bskeys']
    topic = 'topic_mycas'  
    emmtype = '10'
    expiry = '2037-12-31'
    message = f'{device_id}:{bskeys}:{emmtype}:{expiry}'
    try:
        producer.send(topic, message.encode('utf-8')).get()
        logger.info(f"Message sent to Kafka topic {topic}: {message}")
    except KafkaError as e:
        logger.error(f"Failed to send message to Kafka: {e}")
    # Acquire a connection from the pool
    connection = connection_pool.get_connection()

    # Execute the query using the acquired connection
    cursor = connection.cursor()
    insert_query = "INSERT INTO devices (device_id, bskeys) VALUES (%s, %s)"
    data = (device_id, bskeys)
    cursor.execute(insert_query, data)
    connection.commit()
    logger.info((f"device_id: %s bskeys: %s " %(device_id,bskeys)))
    #logger.INFO('device_id: %s, bskeys: %s', device_id, bskeys)
    # Release the connection back to the pool
    cursor.close()
    connection.close()
    flash('Devices added successfully!', 'success')
    flash_messages = json.dumps(dict(get_flashed_messages(with_categories=True)))
    return render_template('index.html', flash_messages=flash_messages)
    #return 'Devices added successfully', 200

if __name__ == '__main__':
    #app.run()
    app.run(port='8000')