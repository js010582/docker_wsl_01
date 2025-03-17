import os
import time

def ping_other():
    # Ping the other container
    response = os.system("ping -c 1 container2")
    
    # Check the response
    if response == 0:
        print("Ping to container2 was successful!")
    else:
        print("Ping to container2 failed.")

if __name__ == "__main__":
    while True:
        ping_other()
        time.sleep(5)  # Ping every 5 seconds 