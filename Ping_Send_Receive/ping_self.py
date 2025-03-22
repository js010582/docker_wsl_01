import os
import socket
import time
import threading
import json

def handle_client(client_socket):
    while True:
        try:
            # Receive data from client
            data = client_socket.recv(1024).decode()
            if not data:
                break
            # Parse the received ping result
            ping_data = json.loads(data)
            print(f"Received from other script: Ping to {ping_data['ip']} {ping_data['status']}")
        except:
            break
    client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 5000))
    server.listen(1)
    print("Server listening on port 5000")
    
    while True:
        client, addr = server.accept()
        print(f"Connected to client: {addr}")
        client_thread = threading.Thread(target=handle_client, args=(client,))
        client_thread.start()

def ping_self():
    # Get the local IP address
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    
    print(f"Starting continuous ping to {local_ip} (Press Ctrl+C to stop)")
    
    # Start server in a separate thread
    server_thread = threading.Thread(target=start_server)
    server_thread.daemon = True
    server_thread.start()
    
    try:
        while True:
            success = os.system(f"ping -c 1 {local_ip}") == 0
            status = 'succeeded' if success else 'failed'
            print(f"Ping to {local_ip} {status}")
            time.sleep(10)
            
    except KeyboardInterrupt:
        print("\nPing stopped by user")

if __name__ == "__main__":
    ping_self()