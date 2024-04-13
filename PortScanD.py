# 185.164.172.184
import socket
import concurrent.futures
from netaddr import iter_iprange

start = input("Enter your start IP: ")
end = input("Enter your end IP: ")
n = int(input("Enter the number of ports to scan: "))
generator = iter_iprange(start, end, step=1)
scan_results = ['Scanning report:\n----------------\n ']


def scan_port(ip, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(0.5)
        try:
            sock.connect((ip, port))
            service = socket.getservbyport(port)
            print(f'{ip}: Port {port} is open ({service}).\n')
            scan_results.append(f'{ip}: Port {port} is open ({service}).\n')
        except:
            pass

#на макс воркерс надо дотестить пока 500 норм.......
with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
    for ip in generator:
        for port in range(1, n+1):
            executor.submit(scan_port, str(ip), port)

print("----\nScanning completed!")


save_to_file = input("Do you want to save the results to the file? (1/0): ")
if save_to_file.lower() == "1":
    filename = input("Enter the filename: ")
    with open(filename, 'w') as file:
        for result in scan_results:
            file.write(result + "\n")
    print("Results saved!")
else:
    print("Exit")
