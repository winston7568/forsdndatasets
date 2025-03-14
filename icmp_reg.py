import os
import platform
import subprocess
import threading

def ping(host):
    # Determine the ping command based on the OS
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '5000', host]
    
    try:
        output = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5000)
        print(output.stdout)
    except subprocess.TimeoutExpired:
        print("Ping timed out after 5000 pings.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    host = input("Enter the host to ping: ")
    ping(host)
