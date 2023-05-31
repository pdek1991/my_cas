import requests

url = 'http://127.0.0.1:5000/generate_osm'

data = {
    'message_id': 818181,
    'message_text': 'Test OSM',
    'device_id': '7010000010'
}

response = requests.post(url, json=data)

if response.status_code == 200:
    print('Message saved successfully')
else:
    print('Failed to save message:', response.text)
