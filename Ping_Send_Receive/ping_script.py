import os
import time
import socket
import json

def connect_to_server():
    # Create a TCP socket for client-server communication
    # AF_INET: IPv4 Internet protocols
    # SOCK_STREAM: TCP socket type for reliable, ordered data transmission
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect(('localhost', 5000))
        return client
    except ConnectionRefusedError:
        print("Could not connect to server. Make sure ping_self.py is running first.")
        return None

def ping_other():
    # Try to connect to the server first
    client = connect_to_server()
    if not client:
        return

    try:
        while True:
            # Ping the other container
            response = os.system("ping -c 1 container2")
            status = 'succeeded' if response == 0 else 'failed'
            
            # Send result to the server
            ping_data = {
                'ip': 'container2',
                'status': status
            }
            client.send(json.dumps(ping_data).encode())
            
            # Print local result
            print(f"Ping to container2 {status}")
            time.sleep(5)  # Ping every 5 seconds
            
    except KeyboardInterrupt:
        print("\nPing stopped by user")
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    ping_other() 