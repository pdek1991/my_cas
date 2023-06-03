import socket

def receiver(multicast_group, port):
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Set the socket options to allow multiple sockets to use the same address and port
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind the socket to the port
    sock.bind(('', port))
    # Join the multicast group
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, socket.inet_aton(multicast_group) + socket.inet_aton('0.0.0.0'))

    # Receive data
    while True:
        data, address = sock.recvfrom(1024)
        print(f"Received: {data.decode('utf-8')} from {address}")

    # Close the socket (this part will never be reached in the above code)
    sock.close()

# Example usage
multicast_group = '224.1.1.1'  # Multicast IP address
port = 5000  # Port number to receive data sent by the cycler function

# Start the receiver
receiver(multicast_group, port)
