import csv
import requests
import concurrent.futures

input_filename = 'input_data.csv'
output_filename = 'output_data.csv'
#url = 'http://192.168.56.115:5050/generate_osm'
url = 'http://127.0.0.1:5050/generate_osm'
num_threads = 1

# Read input data from CSV file
with open(input_filename, 'r') as file:
    reader = csv.DictReader(file)
    input_data = list(reader)

# Function to process a single input data entry and return the result
def process_data(data):
    message_id = data.get('message_id')
    message_text = data.get('message_text')
    device_id = data.get('device_id')
    expiry = data.get('expiry')
    
    response = requests.post(url, json={"message_id": message_id, "message_text": message_text, "device_id": device_id, "expiry": expiry})

    if response.status_code == 200:
        return [message_text, 'Success', response.elapsed.total_seconds()]
    else:
        return [message_text, 'Failure', response.text]

# Process each input data entry and write the output
with open(output_filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Message', 'Response', 'Response Time'])

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        results = executor.map(process_data, input_data)

        for result in results:
            writer.writerow(result)
            print('Message saved successfully') if result[1] == 'Success' else print('Failed to save message:', result[2])

print('Output data saved to', output_filename)
