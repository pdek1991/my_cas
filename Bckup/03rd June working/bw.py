import socket
import time

# Create a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to a server
server_address = ('127.0.0.1', 49599)
sock.connect(server_address)

# Start time
start_time = time.time()
total_bytes = 0
# Receive or send data using the socket
# Replace this with your own logic for receiving or sending data

while True:
    data = sock.recv(1024)  # Receive data
    # data = b"..."  # Send data
    if not data:
        break
    total_bytes += len(data)

# End time
end_time = time.time()

# Calculate elapsed time in seconds
elapsed_time = end_time - start_time

# Calculate bytes per second
bytes_per_sec = total_bytes / elapsed_time

# Print the result
print("Bytes per second:", bytes_per_sec)

# Close the socket
sock.close()
