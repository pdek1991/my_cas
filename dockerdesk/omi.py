from flask import Flask, request
import mysql.connector.pooling

app = Flask(__name__)

# Create a connection pool
db_config = {
    "host": "192.168.56.112",
    "user": "omi_user",
    "password": "omi_user",
    "database": "cas",
}

connection_pool = mysql.connector.pooling.MySQLConnectionPool(pool_name="my_pool", pool_size=10, **db_config)

@app.route('/generate_osm', methods=['POST'])
def generate_osm():
    message_id = request.json['message_id']
    message_text = request.json['message_text']
    device_id = request.json['device_id']
    expiry = request.json['expiry']

    # Acquire a connection from the pool
    connection = connection_pool.get_connection()

    # Execute the query using the acquired connection
    cursor = connection.cursor()
    insert_query = "INSERT INTO generate_osm (message_id, message_text, device_id, expiry) VALUES (%s, %s, %s, %s)"
    data = (message_id, message_text, device_id, expiry)
    cursor.execute(insert_query, data)
    connection.commit()

    # Release the connection back to the pool
    cursor.close()
    connection.close()

    return 'Message saved successfully', 200

@app.route('/addentitlement', methods=['POST'])
def add_entitlement():
    device_id = request.json['device_id']
    package_ids = request.json['package_ids']
    expiry = request.json['expiry']

    # Acquire a connection from the pool
    connection = connection_pool.get_connection()

    # Execute the query using the acquired connection
    cursor = connection.cursor()
    insert_query = "INSERT INTO entitlements (device_id, package_id, expiry) VALUES (%s, %s, %s)"
    for package_id in package_ids:
        data = (device_id, package_id, expiry)
        cursor.execute(insert_query, data)
    connection.commit()

    # Release the connection back to the pool
    cursor.close()
    connection.close()

    return 'Entitlements added successfully', 200

@app.route('/device_keys', methods=['POST'])
def device_keys():
    device_id = request.json['device_id']
    bskeys = request.json['bskeys']

    # Acquire a connection from the pool
    connection = connection_pool.get_connection()

    # Execute the query using the acquired connection
    cursor = connection.cursor()
    insert_query = "INSERT INTO devices (device_id, bskeys) VALUES (%s, %s)"
    data = (device_id, bskeys)
    cursor.execute(insert_query, data)
    connection.commit()

    # Release the connection back to the pool
    cursor.close()
    connection.close()

    return 'Devices added successfully', 200

if __name__ == '__main__':
    #use Container IP here
    app.run(host='172.17.0.2',port='5050')
