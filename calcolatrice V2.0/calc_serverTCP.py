import socket
import json

IP = "127.0.0.1"
PORTA = 65432
DIM_BUFFER = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_server:
    sock_server.bind((IP, PORTA))
    sock_server.listen()

    print(f"Server in ascolto su {IP}:{PORTA}...")

    while True:
        sock_service, address_client = sock_server.accept()

        with sock_service as sock_client:
            dati = sock_client.recv(DIM_BUFFER).decode()

            if not dati:
                continue

            print(f"Ricevuto dal client {address_client}: {dati}")

            # Converti da JSON a dizionario
            dati = json.loads(dati)

            primo = dati["primoNumero"]
            operazione = dati["operazione"]
            secondo = dati["secondoNumero"]

            # Calcolo
            if operazione == "+":
                risultato = primo + secondo
            elif operazione == "-":
                risultato = primo - secondo
            elif operazione == "*":
                risultato = primo * secondo
            elif operazione == "/":
                if secondo != 0:
                    risultato = primo / secondo
                else:
                    risultato = "Errore: divisione per zero"
            else:
                risultato = "Operazione non valida"

            # Invio risultato
            risposta = str(risultato)
            sock_client.sendall(risposta.encode())