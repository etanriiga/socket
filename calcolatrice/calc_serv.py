import socket
import json

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((SERVER_IP, SERVER_PORT))

while True:
    data, addr= s.recvfrom(BUFFER_SIZE)

    if not data:
        break

    data = data.decode()
    data = json.loads(data)

    primoNumero = data["primoNumero"]
    operazione = data["operazione"]
    secondoNumero = data["secondoNumero"]

    if operazione == "+":
        risultato = primoNumero + secondoNumero
    elif operazione == "-":
        risultato = primoNumero - secondoNumero
    else:
        risultato = "Operazione non valida"

    reply = str(risultato)

    s.sendto(reply.encode(), addr)