import csv
import requests

url = "http://192.168.56.11:5000/device_keys"

#locals
#url = "http://127.0.0.1:5050/device_keys"

output_file = open("output.csv", "w", newline="")
csv_writer = csv.writer(output_file)
csv_writer.writerow(["Device ID", "Response", "Response Time"])

with open('bs-keys.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data = {
            "device_id": row['device_id'],
            "bskeys": row['bskeys']
            
        }
        response = requests.post(url, json=data)
        response_time = response.elapsed.total_seconds() if response.elapsed else None
        csv_writer.writerow([row['device_id'], response.text, response_time])

output_file.close()
