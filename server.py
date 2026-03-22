import socket

HOST = '127.0.0.1'
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Server in ascolto...")

conn, addr = server.accept()
print(f"Connesso a {addr}")

data = conn.recv(1024)
print("Ricevuto:", data.decode())

conn.sendall("Messaggio ricevuto".encode())

conn.close()
server.close()