from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)
db = mysql.connector.connect(
    host="192.168.56.112",
    user="omi_user",
    password="omi_user",
    database="cas"
)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/generate_osm', methods=['GET', 'POST'])
def generate_osm():
    message_id = request.form['message_id']
    message_text = request.form['message_text']
    device_id = request.form['device_id']
    expiry = request.form['expiry']

    cursor = db.cursor()
    insert_query = "INSERT INTO generate_osm (message_id, message_text, device_id, expiry) VALUES (%s, %s, %s, %s)"
    data = (message_id, message_text, device_id, expiry)
    cursor.execute(insert_query, data)
    db.commit()

    return 'Message saved successfully'
   
        
    
   

@app.route('/addentitlement', methods=['GET', 'POST'])
def add_entitlement():
    device_id = request.form['device_id']
    package_ids = request.form.getlist('package_ids')
    expiry = request.form['expiry']

    cursor = db.cursor()
    insert_query = "INSERT INTO entitlements (device_id, package_id, expiry) VALUES (%s, %s, %s)"
    for package_id in package_ids:
        data = (device_id, package_id, expiry)
        cursor.execute(insert_query, data)
    db.commit()

    return 'Entitlements added successfully'

@app.route('/device_keys', methods=['GET', 'POST'])
def device_keys():
    device_id = request.form['device_id']
    bskeys = request.form['bskeys']

    cursor = db.cursor()
    insert_query = "INSERT INTO devices (device_id, bskeys) VALUES (%s, %s)"
    data = (device_id, bskeys)
    cursor.execute(insert_query, data)
    db.commit()

    return 'Devices added successfully'

if __name__ == '__main__':
    #Use docker container ip here
    app.run(host='172.17.0.2',port='8081')
    #app.run(host='192.168.56.115', port=80)
    #app.run(port=8081)