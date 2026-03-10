import socket
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, init

init()

target = input("Enter target website or IP: ")

# Convert domain name to IP address
target = socket.gethostbyname(target)

print(Fore.YELLOW + f"\nScanning target: {target}")
print("Scanning ports 1 - 1024\n")

def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = s.connect_ex((target, port))

        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknown"

            print(Fore.GREEN + f"Port {port} OPEN ({service})")

        s.close()

    except:
        pass


with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(scan_port, range(1,1025))


print(Fore.CYAN + "\nScan completed!")