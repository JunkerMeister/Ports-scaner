import socket
import threading

ip = input("Enter your IP: ")
n = int(input("Enter the number of ports to scan: "))
scan_results = []

def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    try:
        sock.connect((ip, port))
        service = socket.getservbyport(port)
        print(f'Port {port} is open ({service}).\n')
        scan_results.append(f'Port {port} is open ({service}).')
        sock.close()

    except:
        pass

threads = []
for i in range(n):
    potoc = threading.Thread(target=scan_port, args=(ip, i))
    potoc.start()
    threads.append(potoc)

for thread in threads:
    thread.join()

print("----\nScanning completed!")

save_to_file = input("Do you want to save the results to the file? (1/0): ")
if save_to_file.lower() == "1":
    filename = input("Enter the filename: ")
    with open(filename, 'w') as file:
        for result in scan_results:
            file.write(result + "\n")
    print("Results saved!.")
else:
    print("Exit")
