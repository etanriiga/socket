import socket
import json

HOST = '127.0.0.1'
PORT = 65432
BUFFER_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_service:
    sock_service.connect((HOST, PORT))

    # Input utente
    primoNumero = float(input("Inserisci il primo numero: "))
    operazione = input("Inserisci operazione (+, -, *, /): ")
    secondoNumero = float(input("Inserisci il secondo numero: "))

    # Creazione messaggio JSON
    messaggio = {
        "primoNumero": primoNumero,
        "operazione": operazione,
        "secondoNumero": secondoNumero
    }

    messaggio = json.dumps(messaggio)

    # Invio
    sock_service.sendall(messaggio.encode())

    # Ricezione risposta
    data = sock_service.recv(BUFFER_SIZE)

print("Risultato:", data.decode())