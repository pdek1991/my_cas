from flask import Flask, request
import mysql.connector
import threading

app = Flask(__name__)
db = mysql.connector.connect(
    host="192.168.56.112",
    user="omi_user",
    password="omi_user",
    database="cas"
)

@app.route('/generate_osm', methods=['POST'])
def generate_osm():
    message_id = request.json['message_id']
    message_text = request.json['message_text']
    device_id = request.json['device_id']
    expiry = request.json['expiry']

    cursor = db.cursor()
    insert_query = "INSERT INTO generate_osm (message_id, message_text, device_id, expiry) VALUES (%s, %s, %s, %s)"
    data = (message_id, message_text, device_id, expiry)
    cursor.execute(insert_query, data)
    db.commit()

    return 'Message saved successfully', 200

@app.route('/addentitlement', methods=['POST'])
def add_entitlement():
    device_id = request.json['device_id']
    package_ids = request.json['package_ids']
    expiry = request.json['expiry']

    cursor = db.cursor()
    insert_query = "INSERT INTO entitlements (device_id, package_id, expiry) VALUES (%s, %s, %s)"
    for package_id in package_ids:
        data = (device_id, package_id, expiry)
        cursor.execute(insert_query, data)
    db.commit()

    return 'Entitlements added successfully', 200

@app.route('/device_keys', methods=['POST'])
def device_keys():
    device_id = request.json['device_id']
    bskeys = request.json['bskeys']
   

    cursor = db.cursor()
    insert_query = "INSERT INTO devices (device_id, bskeys) VALUES (%s, %s)"
    data = (device_id, bskeys)
    cursor.execute(insert_query, data)
    db.commit()

    return 'Devices added successfully', 200

thread_local = threading.local()

@app.teardown_appcontext
def close_db(error):
    if hasattr(thread_local, 'db'):
        thread_local.db.close()

@app.before_request
def before_request():
    if not hasattr(thread_local, 'db'):
        thread_local.db = db.cursor()
    else:
        if not thread_local.db.is_connected():
            thread_local.db = db.cursor()

if __name__ == '__main__':
    app.run()
