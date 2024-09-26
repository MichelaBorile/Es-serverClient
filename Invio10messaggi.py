import socket

client_address  = ("localhost", 6980)   #localhost = ip del server

BUFFER_SIZE = 4092 #ricevo dei dati o li invio, devo dichiare quanti bit posso usare

udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #DGRAM socket udp

udp_client_socket.bind(client_address)