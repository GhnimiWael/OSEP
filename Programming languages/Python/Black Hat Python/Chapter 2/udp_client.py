import socket

target_host = "127.0.0.1"
target_port = 9997

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send some data
client.sendto(b"AAAABCCCCC", (target_host, target_port))

# receive some data
data, add = client.recvfrom(4094)

print(dat.decode())
client.close()