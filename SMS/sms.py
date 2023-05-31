import requests

url = 'http://192.168.56.115:5050/generate_osm'

data = {
    'message_id': 818181,
    'message_text': 'Test OSM',
    'device_id': '7010000010',
    'expiry': '2023-05-23'
}

response = requests.post(url, json=data)

if response.status_code == 200:
    print('Message saved successfully')
else:
    print(response.status_code)
    print('Failed to save message:', response.text)
