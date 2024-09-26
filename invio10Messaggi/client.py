import socket

server_address  = ("localhost", 6982)   #localhost = ip del server

BUFFER_SIZE = 4092 #ricevo dei dati o li invio, devo dichiare quanti bit posso usare

udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #DGRAM socket udp

udp_client_socket.bind(server_address)

message = "ciao server"

for i in range(0, 9):
    udp_client_socket.sendto(message.encode(), server_address)

udp_client_socket.close()