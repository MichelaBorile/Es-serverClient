import socket

server_address = ("10.210.0.59", 6981)


tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_server_socket.bind(server_address)

tcp_server_socket.connect(server_address)

tcp_server_socket.listen(1)
conn, addr = tcp_server_socket.accept()
data = conn.recv(4096)
conn.sendall("Messaggio ricevuto!")

