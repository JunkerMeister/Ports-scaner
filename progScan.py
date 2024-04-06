import socket
import threading

ip = input("Enter your IP: ")
n = int(input("Enter the number of ports to scan: "))
def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    try:
        connect = sock.connect((ip, port))
        service = socket.getservbyport(port)
        print(f'Port {port} is open ({service}).\n')
        sock.close()
        print('----')
    except:
        pass

for i in range(n):
    potoc = threading.Thread(target=scan_port, args=(ip, i))
    potoc.start()
print("Scanning complited!")