import socket
import threading

def main():
    server_address = ("localhost", 6980)
    BUFFER_SIZE = 4092
    client_address = udp_server_socket.recvfrom(BUFFER_SIZE)
    udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_server_socket.bind(server_address)
    thread_invio = threading.Thread(target=invio, args=(udp_server_socket))
    thread_ricezione = threading.Thread(target=ricezione, args=(udp_server_socket))
    thread_ricezione.start()
    thread_invio.start()

def ricezione(udp_server_socket, BUFFER_SIZE):
    while(True):
        data, address = udp_server_socket.recvfrom(BUFFER_SIZE)
        print(f"messaggio ricevuto: {data.decode()} da {address}")
def invio(client_address, udp_server_socket):
    while(True):
        messaggio = input("")
        udp_server_socket.sendto(messaggio.encode(), client_address)

print(__name__)
if __name__ == "__main__":
    main()