import socket

server_address = ("10.210.0.59", 6981)


tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_client_socket.connect(server_address)

messaggio = input("Scrivi l'operazione che vuoi fare e il livello in cui mandare il comando separato da una virgola: ")

tcp_client_socket.sendto(messaggio.encode(), server_address)

# tcp_client_socket.listen()
# conn, addr = tcp_client_socket.accept()
# data = conn.recv(4096)

# print(data.encode())
