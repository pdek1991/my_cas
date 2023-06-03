import csv
import requests
url = 'http://192.168.56.11:5000/generate_osm'
#url = 'http://127.0.0.1:5050/generate_osm'

with open('input_data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data = {
            "message_id": row['message_id'],
            "message_text": row['message_text'],
            "device_id": row['device_id'],
            "expiry": row['expiry'],
            
        }


        response = requests.post(url, json=data)

    if response.status_code == 200:
        print('Message saved successfully')
    else:
        print(response.status_code)
        print('Failed to save message:', response.text)
