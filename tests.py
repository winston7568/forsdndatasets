import subprocess

def run_iperf(server, duration=10, port=5201, bandwidth='1M'):
    try:
        command = ['iperf3', '-c', server, '-t', str(duration), '-p', str(port), '-b', bandwidth]
        output = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(output.stdout)
    except Exception as e:
        print(f"An error occurred: {e}")

def run_hping3_udp(target, port=80, packet_count=1000):
    try:
        command = ['hping3', '--udp', '-p', str(port), '--flood', '--count', str(packet_count), target]
        subprocess.run(command)
    except Exception as e:
        print(f"An error occurred: {e}")

def run_hping3_icmp(target, packet_count=1000):
    try:
        command = ['hping3', '--icmp', '--flood', '--count', str(packet_count), target]
        subprocess.run(command)
    except Exception as e:
        print(f"An error occurred: {e}")

def run_hping3_tcp(target, port=80, packet_count=1000):
    try:
        command = ['hping3', '--syn', '-p', str(port), '--flood', '--count', str(packet_count), target]
        subprocess.run(command)
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    print("Select the test you want to run:")
    print("1. iperf3 (Bandwidth test)")
    print("2. UDP flood")
    print("3. ICMP flood")
    print("4. TCP SYN flood")
    
    choice = int(input("Enter the number of the test: "))
    
    if choice == 1:
        server = input("Enter the IP or hostname of the iperf server: ")
        duration = int(input("Enter test duration (seconds): "))
        port = int(input("Enter server port (default 5201): "))
        bandwidth = input("Enter bandwidth (default 1M): ")
        run_iperf(server, duration, port, bandwidth)
    elif choice == 2:
        target = input("Enter the target IP for UDP flood: ")
        udp_port = int(input("Enter target UDP port (default 80): "))
        packet_count = int(input("Enter number of packets to send: "))
        run_hping3_udp(target, udp_port, packet_count)
    elif choice == 3:
        target = input("Enter the target IP for ICMP flood: ")
        packet_count = int(input("Enter number of packets to send: "))
        run_hping3_icmp(target, packet_count)
    elif choice == 4:
        target = input("Enter the target IP for TCP SYN flood: ")
        tcp_port = int(input("Enter target TCP port (default 80): "))
        packet_count = int(input("Enter number of packets to send: "))
        run_hping3_tcp(target, tcp_port, packet_count)
    else:
        print("Invalid choice. Please select a valid test number.")
