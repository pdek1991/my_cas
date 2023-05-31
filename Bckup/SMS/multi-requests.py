import csv
import requests

input_filename = 'input_data.csv'
output_filename = 'output_data.csv'
url = 'http://127.0.0.1:5000/generate_osm'

# Read input data from CSV file
# Process each input data entry and write the output
with open(output_filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Message', 'Response', 'Response Time'])

    with open(input_filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            message_id = row.get('message_id')
            message_text = row.get('message_text')
            device_id = row.get('device_id')
            
            response = requests.post(url, json={"message_id": message_id, "message_text": message_text, "device_id": device_id})

            if response.status_code == 200:
                writer.writerow([message_text, 'Success', response.elapsed.total_seconds()])
                print('Message saved successfully')
            else:
                writer.writerow([message_text, 'Failure', response.text])
                print('Failed to save message:', response.text)

print('Output data saved to', output_filename)
