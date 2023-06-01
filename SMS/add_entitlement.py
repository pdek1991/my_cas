import csv
import requests

#url = "http://192.168.56.115:5050/addentitlement"
#Local
url = "http://127.0.0.1:5050/addentitlement"

output_file = open("output.csv", "w", newline="")
csv_writer = csv.writer(output_file)
csv_writer.writerow(["Device ID", "Response", "Response Time"])

with open('packages.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data = {
            "device_id": row['device_id'],
            "package_ids": row['package_ids'].split(':'),
            "expiry": row['expiry']
        }
        response = requests.post(url, json=data)
        response_time = response.elapsed.total_seconds() if response.elapsed else None
        csv_writer.writerow([row['device_id'], response.text, response_time])

output_file.close()
