# Client TCP multithread che invia NUM_WORKERS richieste contemporanee al server
# Ogni richiesta contiene un'operazione aritmetica da eseguire

import socket         # Per la comunicazione di rete
import json           # Per la codifica/decodifica JSON
import random         # Per generare numeri casuali
import time           # Per misurare i tempi di esecuzione
import threading      # Per gestire l'esecuzione parallela (multithreading)

# --- Configurazione ---
HOST = "127.0.0.1"           # IP del server
PORT = 22224                # Porta del server (assicurarsi che il server stia ascoltando su questa)
NUM_WORKERS = 15            # Numero di richieste (thread) da inviare in parallelo
OPERAZIONI = ["+", "-", "*", "/", "%"]  # Lista delle operazioni consentite

#1 Funzione che genera e invia richieste al server, e riceve le risposte
def genera_richieste(address, port):
    #2 Crea un socket TCP e si connette al server (il socket viene chiuso automaticamente alla fine del blocco "with")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_service:
        sock_service.connect((address, port))  # Connessione al server

        #3 genera due numeri e un'operazione casuali da inviare al server per ogni richiesta (continua a generare richieste finché il thread è attivo)  
        primoNumero = random.randint(0, 100)
        operazione = OPERAZIONI[random.randint(0, 3)]  # Sceglie operazione a caso (tra le prime 4)
        secondoNumero = random.randint(0, 100)

        #4 Crea un dizionario con i dati della richiesta, lo codifica in JSON e lo invia al server (sfruttando la connessione TCP stabilita) 
        messaggio = {
            "primoNumero": primoNumero,
            "operazione": operazione,
            "secondoNumero": secondoNumero
        }
        messaggio = json.dumps(messaggio)

        #5 Invia il messaggio al server e attende la risposta (il tempo di attesa della risposta sarà misurato per ogni thread) 
        sock_service.sendall(messaggio.encode("UTF-8"))

        #6 Inizia a misurare il tempo di esecuzione del thread (dalla richiesta al server fino alla ricezione della risposta) 
        start_time_thread = time.time()

        #7 Ricevi la risposta dal server (il tempo di attesa della risposta sarà misurato per ogni thread) 
        data = sock_service.recv(1024)

    #8 Termina la misurazione del tempo di esecuzione del thread e stampa il risultato ricevuto dal server insieme al tempo impiegato per eseguire la richiesta (dalla richiesta al server fino alla ricezione della risposta) 
    end_time_thread = time.time()
    print("Received: ", data.decode())
    print(f"{threading.current_thread().name} exec time = ", end_time_thread - start_time_thread)

# --- Punto di ingresso del programma ---
if __name__ == "__main__":
    start_time = time.time()  # Tempo di inizio totale

    #9 Crea una lista di thread che eseguiranno la funzione genera_richieste in parallelo (ogni thread invierà una richiesta al server) 
    threads = [
        threading.Thread(target=genera_richieste, args=(HOST, PORT))
        for _ in range(NUM_WORKERS)
    ]

    #10 Avvia tutti i thread creati (in modo che inizino a inviare le richieste al server in parallelo) 
    [thread.start() for thread in threads]

    #11 Attendi che tutti i thread completino la loro esecuzione (in modo da assicurarti che tutte le richieste siano state inviate e tutte le risposte siano state ricevute prima di terminare il programma) 
    [thread.join() for thread in threads]

    end_time = time.time()  # Tempo di fine totale

    # Stampa il tempo complessivo impiegato per eseguire tutte le richieste
    print("Tempo totale impiegato = ", end_time - start_time)