#server e client che comunicano tra loro, dobbiamo sapere il nostro indirizzo ip e quello del server 
# --> client non deve sapere il suo basta che il server sappia il proprio
#variabili parlanti

import socket

server_address  = ("10.210.0.29", 6980)   #localhost = ip del server

BUFFER_SIZE = 4092 #ricevo dei dati o li invio, devo dichiare quanti bit posso usare

udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #DGRAM socket udp

udp_server_socket.bind(server_address)
print("sono in ascolto")
data, address = udp_server_socket.recvfrom(BUFFER_SIZE)     #mette in ascolto, BLOCCANTE, il programma si ferma. mi metto in ascolto sulla porta, con il mio indirizzo ip --> quando mi arrivano i dati, indiirizzo lo metto in address, il resto in data

print(f"Messaggio ricevuto: {data.decode()} da {address}")    #client deve fare endcode

if (data != None):
    message = "Ho ricevuto il tuo messaggio!".encode()
else:
    message = "Il tuo messaggio è vuoto".encode()

udp_server_socket.sendto(message, server_address)

#altro modo es con b"" ma poi non posso fare le {data}