import socket

HOST = '127.0.0.1'
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

msg = "Hello Server"
client.sendall(msg.encode())

data = client.recv(1024)
print("Risposta server:", data.decode())

client.close()