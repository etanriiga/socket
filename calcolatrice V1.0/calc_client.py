
import json





import socket

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005
BUFFER_SIZE =1024
NUM_MESSAGES= 5

#Creazione del socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

primoNumero= (float(input("inserisci il primo numero: ")))
operazione = input("Inserisci l'operazione  (simbolo)")
secondoNumero = (float(input("inserisci il secondo numero: ")))
messaggio = {"primoNumero": primoNumero,
             "operazione": operazione,
             "secondoNumero": secondoNumero
}
messaggio = json.dumps(messaggio)
s.sendto(messaggio.encode("UTF-8"), (SERVER_IP, SERVER_PORT))
data, address =s.recvfrom(BUFFER_SIZE)

print("Risultato:", data.decode())
#Chiusura del socket
s.close()