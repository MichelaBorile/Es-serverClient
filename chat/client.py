import socket

server_address  = ("localhost", 6981)   #localhost = ip del server

BUFFER_SIZE = 4092 #ricevo dei dati o li invio, devo dichiare quanti bit posso usare

udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #DGRAM socket udp

udp_client_socket.bind(server_address)

message = input("Inserisci il messaggio da inviare al server: ")

udp_client_socket.sendto(message.encode(), server_address)
data, address = udp_client_socket.recvfrom(BUFFER_SIZE)

print(f"Risposta server: {data.decode()}")

udp_client_socket.close()


def main():
    udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #DGRAM socket udp
    udp_client_socket.sendto()