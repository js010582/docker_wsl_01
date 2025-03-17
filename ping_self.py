import os
import socket

def ping_self():
    # Get the local IP address
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    
    # Ping the local IP address
    response = os.system(f"ping -c 1 {local_ip}")
    
    # Check the response
    if response == 0:
        print(f"Ping to {local_ip} was successful!")
    else:
        print(f"Ping to {local_ip} failed.")

if __name__ == "__main__":
    ping_self() 